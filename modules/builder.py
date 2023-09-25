import shutil
import os
import pathlib

import modules.config as config

import modules.api as api
import modules.file as file
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
		except:
			log.error(f"An unknwon error occured when opening file '{path}'.")

		self.content = file.read()
		self.path = path

	def extension(self):
		return self.path.rsplit('.', 1)[-1]

	def name(self):
		return self.path.rsplit('/', 1)[-1]

	def full_name(self):
		pass

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

		self.ready()


	def ready(self):
		"""
		Overwriteable method that runs on initalization,
		"""
		pass


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

	# Please overwrite us!
	# vvvvvvvvvvvvvvvvvvvv

	def build(self, file):
		"""
		Overwriteable method that builds content files.
		"""
		
		pass


	def finalize(self, file):
		"""
		Overrideable method that is by default called at the end of consturction.
		"""


	def copy(self, path: str):
		"""
		Overwriteable method that copies a file.
		"""
		# shutil.copyfile(child, get_output_variant(child))


	def complete(self):
		"""
		Overwriteable method that runs after all files have been built. This does not by default run when serving.
		"""
		pass


def build_all():
	"""
	Loops over every file in the main directory for the input content directory.
	Create the output directory if the output directory does not exist and
	the input content directory was found. 
	Search for buildable files if the input content directory was found.
	"""
	for child in pathlib.Path().iterdir():
		# We do not need to check for files if it is the content directory
		if (child.name != config.content.directory): continue

		# Make sure it is not a file named the same as the content directory
		if (os.path.isfile(child) == True): continue

		# Create the directory for output
		api.create_output_directory()

		build_all_files(child, 0)


def build_all_files(child, recursion):
	"""
	Recursively iterates over the current contents of a directory.
	
	If it is a directory that does not yet exist in the output, create the
	output file.
	
	If it is a file that is the correct file extension and the output files
	modify date is younger then the input, build a new file to output. If the
	file is older, then ignore.
	
	If a file is the wrong extension, do the same actions but copy the file
	instead of building.
	"""
	recursion += 1

	if recursion >= config.max_recursion:
		log.fatal("Recursion limit exeeded: build failed! core.py:build_all_files")
		exit()

	for child in pathlib.Path(child).iterdir():
		if os.path.isdir(child) == True:
			api.confirm_output_exists()

			build_all_files(child, recursion)
			continue

		if config.content.extensions.__contains__(child.suffix):
			# build_file(str(child))
			pass
		# Else if the file is a mentioned compilation only file, compile it
		elif config.components.extensions.__contains__(child.suffix):
			# htcl_compile(str(child))
			pass
		else: # This should be files such as images, JS documents, and others
			shutil.copyfile(child, api.get_output_variant(child))
			# log.copied(f"{child}")