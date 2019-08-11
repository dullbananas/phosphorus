class Response:
	def __init__(self,
		content,
		status='200 OK',
		headers=None,
		content_type='text/html',
	):
		self.content = content
		self.status = status
		if headers == None:
			self.headers = {}
		else:
			self.headers = headers
		self.headers['Content-type'] = content_type
