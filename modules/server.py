from http.server import BaseHTTPRequestHandler as BaseHttpRequestHandler

import builder_modules.config as config
from builder import build as build
from builder_modules.core_classes import File

METHOD_NOT_ALLOWED = 405

class LiveServer(BaseHttpRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		try:
			build(File(f"{config.content.directory}{self.path.rstrip('/')}.md"))
		except IsADirectoryError:
			build(File(f"{config.content.directory}{self.path}/index.md"))

		path = f"{config.output.directory}{self.path}"

		try:
			content = open(f"{path}", "r").read()
		except IsADirectoryError:
			content = open(f"{path}/index.html", "r").read()

		self.wfile.write(bytes(f"{content}", "utf-8"))

	def do_HEAD(self):
		self.send_response(METHOD_NOT_ALLOWED)
	
	def do_POST(self):
		self.send_response(METHOD_NOT_ALLOWED)
	
	def do_PUT(self):
		self.send_response(METHOD_NOT_ALLOWED)
	
	def do_DELETE(self):
		self.send_response(METHOD_NOT_ALLOWED)
	
	def do_PATCH(self):
		self.send_response(METHOD_NOT_ALLOWED)