# The API you have access to by default in <?py/> blocks. This is also
# largely used by builder core and in your userspace file.

import os
import pathlib

import time

import modules.config as config

# NOTE TO FUTURE ME:
# Most of these things should not be in the API! They should be elsewhere! Pretty much only This fits in here.

class This:
	def __init__(
		url: str,
	):
		pass
		# give tis all the data that is accessed via the api

	def modified_datetime():
		"""
		TODO. Returns a struct_time [?maybe? theres no time class which is stupid...] in UTC.
		"""
		pass

def confirm_output_exists(path):
	if os.path.exists(get_output_variant(path)) == True:
		return

	os.mkdir(get_output_variant(path))

def get_output_variant(path: str) -> str:
	"""
	Takes a path to a file and replaces the first case of the input directory
	with the output directory to create the output files path.
	"""
	return str(path).replace(config.content.directory, config.output.directory, 1)


def create_output_directory():
	if os.path.isdir(config.output.directory) == True:
		return
	
	os.mkdir(config.output.directory)

def htcl(string: str):
	"""
	Insert the provided HTCL string into the page. This will be compiled
	fully into components in a later step.

	WARNING: NOT IMPLEMENTED!
	"""

def html(string: str):
	"""
	Insert the provided HTML string into the page. This will NOT be
	further compiled at a later stage, consider using `insert_htcl`
	if you want to use components.

	WARNING: NOT IMPLEMENTED!
	"""

def text(string: str):
	"""
	Insert the provided text string into the page. All HTML and
	HTCL

	WARNING: NOT IMPLEMENTED!
	"""

def paginate(per_page: int):
	"""
	Paginate the post list into multiple pages, with the `per_page` argument
	being used to determine how many are on each page.

	NOTE: This function does not actually handle pagination, and is instead
	a signal to the rest of the builder on how to paginate content, thus its
	behavour cannot be replicated.
	"""

def get_posts_from_tag(number, *, tag="untagged", offset=0):
	"""
	Gets <number> pages from the provided tag starting at the
	offset.
	"""

	pass