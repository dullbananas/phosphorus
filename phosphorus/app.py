from . import utils, pages
import re


class Endpoint:
	def __init__(self, pattern, func):
		self.pattern = re.compile(pattern)
		self.func = func


	def match(self, url):
		return self.pattern.match(url)


	def call(self, **kwargs):
		return self.func(**utils.filter_args(self.func, kwargs))



class App:
	def __init__(self):
		self.endpoints = []


	def add_endpoint(self, pattern):
		def decor(f):
			self.endpoints.append(Endpoint(pattern, f))
			return f
		return decor


	def wsgi_app(self, environ, start_response):
		# Get matching endpoint
		match = None
		for endpoint in self.endpoints:
			match = endpoint.match(environ['PATH_INFO'])
			if match:
				break

		# 404 error if no endpoint matches
		if not match:
			start_response('404 Not Found', [('Content-Type', 'text/html')])
			return pages.NOT_FOUND

		# Call function
		response = endpoint.call(
			match=match,
			environ=environ,
		)

		# Process response and produce actual response
		start_response(response.status, [i for i in response.headers.items()])
		print([i for i in response.headers.items()])
		return [bytes(response.content, 'utf-8')]


	def __call__(self, environ, start_response):
		result = self.wsgi_app(environ, start_response)
		print(result)
		return result
