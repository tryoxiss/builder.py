import shutil
import os
import pathlib
import platform

import modules.config as config

import modules.api as api
import modules.log as log

from modules.decorators import expect as expect

import modules.htcl
import modules.modern_markdown


class File:
	content: str = ""
	path: str = ""

	def __init__(self, path):
		# WARNING NERDS:
		# this only works given a name and not a path. :c
		try:
			file = open(path)
		except FileNotFoundError:
			log.error(f"File '{path}' does not exist.")
			return
		except:
			log.error(f"An unknwon error occured when opening file '{path}'.")
			return

		self.content = file.read()
		self.path = str(path)


	def extension(self):
		return f".{self.path.rsplit('.', 1)[-1]}"


	def name(self):
		return self.path.rsplit(config.OS_PATH_DELIMINATOR, 1)[-1]


	def full_name(self):
		pass


	def path_only(self):
		return self.path.rstrip(self.name())


	def make_path_fancy(self, path: str) -> str:
		"""
		Note: normally it goes to {path}/index.html, but if you had
		/posts/kittentd-devlog-1/
			   kittentd-devlog-1.md
			   screenshot1.png
			   (etc)
		
		then it would get written to /posts/kittentd-devlog-1/kittentd-devlog-1/index.html, which is ugly. So if the files name
		is the same as the directories or is `index` we want it to not create another directory.
		
		we also want to allow for pattersn like /posts/12/sep/2023/ and allow writing to multiple locations.
		
		This function SHOULD address this!
		"""

		if path.endswith(f"index.{self.extension()}"):
			path = path.rstrip(f"index.{self.extension()}")
			print("ends in index.<extension>")
		
		print(f"{self.name().rstrip(self.extension())}/{self.name()}")


		# This bit is a bit ew but basically if its something like
		# */name1/name1.* then we just strip the end bit and replace
		# it with index.html to make it work the way we want it to.

		# example:
		# posts/post-name/post-name.md
		if path.endswith(f"{self.name().rstrip(self.extension())}/{self.name()}"):
			path = f"{path.rstrip(self.name())}index"
			print(path)

		return path


	def write(self, path: str, fancy=True) -> None:
		"""
		Writes a compiled file to the absolute path provided. If fancy is true, it will
		use the latest in blood sweat and tears technology to add a trailing / to the end
		of the URL and prevent weird doubble ups like `/posts/post-name/post-name.html`.

		This lets you more easily put media in the same directory as your post, for example
		/posts/post-name/ could contain figure1.png and post-name.md or index.md and still
		show up at /posts/post-name/. I find it an easier way to deal with media for articles,
		at least.

		[!] DANGER: This function is blind! It will overwrite anything at the desired path!
		"""

		if fancy == True:
			path = self.make_path_fancy(path)

		os.makedirs(self.path_only(), exist_ok=True)

		file = open(f"{path.rstrip(self.extension())}.html", "w")
		file.write(self.content)
		file.close()


class Builder:

	# Lets us define nice namespaces such as
	# self.config.content.directory
	
	CACHE_LOCATION = ".buildercache"

	api = api

	def __init__(
		self,
		*,
		template_engine=modules.htcl.HtclCompiler,
		content_compiler=modules.modern_markdown.ModernMarkdownCompiler
	):
		"""
		Initalize the builder class. DO NOT OVERWRITE! Use ready() instead!
		"""
		
		self.template_engine = template_engine()
		self.content_compiler = content_compiler()

		if os.path.isdir(config.output.directory) == False:
			os.mkdir(config.output.directory)

		self.ready()
		self.validate()


	def ready(self):
		"""
		Overwriteable method that runs on initalization,
		"""
		pass


	def validate(self):
		pass
		# make sure inputs are valid


	def construct(self):
		"""
		Make a release build of the site.
		"""


	def blueprint(self, *, ip: str = "127.0.0.1", port: int = 8080):
		"""
		Serve a developement version of the site.
		"""
		self.serve(ip=ip, port=port)


	def serve(self, *, ip: str = "127.0.0.1", port: int = 8080):
		pass
		# serving code


	def build_all(self, recursion, child=config.content.directory):
		"""
		Recursively iterates over the current contents of the provided directory and runs
		either the build, copy, or compile functions on them based on its extension.
		"""
		recursion += 1

		if recursion >= config.max_recursion:
			log.fatal("Recursion limit exeeded: build failed! core.py:build_all_files")

		for child in pathlib.Path(child).iterdir():
			if os.path.isdir(child) == True:
				api.confirm_output_exists(str(child))
				self.build_all(recursion, child=child)
				continue

			self.handle_buildable_file(child)


	def handle_buildable_file(self, path):

		if path.suffix in config.content.extensions:
			# try:
			self.build(File(path))
			# except:
				# log.error("build() function invalid.")

		elif path.suffix in config.components.extensions:
			try:
				self.build_template(path)
			except:
				log.error("build_template() function invalid.")

		else:
			try:
				self.copy(path)
			except:
				log.error("copy() function invalid.")

	# Please overwrite us!
	# vvvvvvvvvvvvvvvvvvvv

	def build_template(self, path):
		print(f"Template: {path}")


	def build(self, file: File):
		"""
		Overwriteable method that builds content files.
		"""
		print(f"---->> {file.path.rstrip(' ')}")

		file.content = self.content_compiler.feed(file.content)

		file.write(api.get_output_variant(file.path))


	def finalize(self):
		"""
		Overrideable method that is by default called at the end of consturction.
		"""


	def copy(self, path: str):
		"""
		Overwriteable method that copies a file.
		"""

		# api.confirm_output_exists(path)

		shutil.copyfile(path, api.get_output_variant(path))


	def complete(self):
		"""
		Overwriteable method that runs after all files have been built. This does not by default run when serving.
		"""
		pass