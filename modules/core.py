__version__ = '0.0.3'

import pathlib
import os
import shutil
import time

# from runme import build as build
import modules.log as log
import modules.config as config
import modules.htcl as parser

from modules.decorators import expect as expect
from modules.server import LiveServer
from http.server import HTTPServer as HttpServer

builder_cache_location = ".buildercache"

def run(*, ip="127.0.0.1", port=8080, lan=False):
    """
    This is abstracted for future modification of the running process.
    This will allow for a constantly running server to edit and see changes
    live later.
    """

    # server = HttpServer((ip, port), LiveServer)

    # log.intro(ip, lan)
    # server.serve_forever()

    # We run a method to serve the files, so maybe for live server we can just build them as they are requested?

    build_all()

def build_release():
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
		create_output_directory()

		build_all_files(child, 0)

def create_output_directory():
	if os.path.isdir(config.output.directory) == False:
		os.mkdir(config.output.directory)

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
		# If the path is a directory,
		# we need to search in that directory for more files to build
		if os.path.isdir(child) == True:
			confirm_output_exists()

			build_all_files(child, recursion)
			continue

		# Need to add an option to rebuild all files on release build
		# If a file hasn't been edited after the previous build time, continue
		# if os.path.getmtime(get_output_file(child)) >= os.path.getmtime(child):
		#	 continue

		# If the file has a mentioned content file extention, build it
		if config.content.extensions.__contains__(child.suffix):
			build_file(str(child))
		# Else if the file is a mentioned compilation only file, compile it
		elif config.components.extensions.__contains__(child.suffix):
			htcl_compile(str(child))
		else: # This should be files such as images, JS documents, and others
			shutil.copyfile(child, get_output_variant(child))
			log.copied(f"{child}")

@expect("There is either no `build()` function in builder.py or it contains errors.")
def build_file(file_path):
	build( classes.File(str(file_path)) )
	log.built(f"{file_path}")

def htcl_compile(file_path):
	parser.compile( classes.File(str(file_path)) )
	log.built(f"{file_path}")

def confirm_output_exists(item):
	if os.path.exists(get_output_variant(item)) == False:
		os.mkdir(get_output_variant(item))

def get_output_variant(path: pathlib.Path) -> str:
	"""
	Takes a path to a file and replaces the first case of the input directory
	with the output directory to create the output files path.
	"""
	return str(path).replace(config.content.directory, config.output.directory, 1)