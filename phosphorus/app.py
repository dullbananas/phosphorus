from . import utils, pages
import re


class Endpoint:
	def __init__(self, pattern, func, flags=0):
		self.pattern = re.compile(pattern, flags)
		self.func = func


	def match(self, url):
		return self.pattern.fullmatch(url)


	def call(self, **kwargs):
		return self.func(**utils.filter_args(self.func, kwargs))



class App:
	def __init__(self):
		self.endpoints = []


	def add_endpoint(self, pattern, re_whitespace=False):
		flags = re.VERBOSE if re_whitespace else 0
		def decor(f):
			self.endpoints.append(Endpoint(pattern, f, flags))
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
			return [pages.NOT_FOUND]

		# Call function
		response = endpoint.call(
			match=match,
			environ=environ,
		)

		# Process response and produce actual response
		start_response(response.status, [i for i in response.headers.items()])
		return [bytes(response.content, 'utf-8')]


	def __call__(self, environ, start_response):
		result = self.wsgi_app(environ, start_response)
		return result
