# The API you have access to by default in <?py/> blocks.

import builder_modules.core_classes as classes

def meow():
	print("Mewooo!!")

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

def get_posts_from_tag(number, *, tag="untagged", offset=0) -> list[classes.File]:
	"""
	Gets <number> pages from the provided tag starting at the
	offset.
	"""

	pass