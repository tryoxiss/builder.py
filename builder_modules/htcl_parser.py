import builder_modules.core_classes as classes

from builder_modules.html_parser import HTMLParser as HtmlParser

def compile(file: classes.File):
	"""
	The compiler interface for HTCL
	"""

	compiler = HtclTemplate()
	compiler.feed(file.content)

# NOTE TO KHAIM:
# Scropes styles are done with a class added to all sectors in an object, and are per unique component.
# As in, two <Button>s don't need to have diffrent scopes or even re-inject styles since they are the
# same. As long as they are unique. I might try a class called `.scope_ComponentName` though? Since
# you can only have one component named the same thing, that should be gaurnteed to be unique.

class HtclTemplate(HtmlParser):
	depth = 0

	component_content = ""
	component = [] # Lists of components, in order. Last is most recent.

	# def _is_component(self, name):
	# 	if len(name) >= 1:
	# 		return name[0].isupper()
	# 	else:
	# 		return False

	def handle_starttag(self, tag, attrs):
		self.depth += 1

		if tag == 'slot':
			# Manage inserting content
			print("WARNING: `slot` MUST be self closing, try `<slot />`")
			return
		else:
			print("Encountered a start tag:", tag)

	def handle_endtag(self, tag):
		self.depth -= 1

		if tag == 'slot':
			return # Its handled when you open it, so nothing to do!
		else:
			print("Encountered a end tag:", tag)

	def handle_data(self, data):

		# girls if your data starts with "{"
		# And ends with "}"
		# THIS ONLY READS THE START/END THIS WAY! We NEED to be able
		# to find variables inside longer strings like {api.page.title} * mywebsite.tld
		if data.startswith("{") and data.endswith("}"):
			# Thats not your data
			# Thats a variable!
			pass

		print("Encountered some data  :", data)

	def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
		if tag == "slot":
			print("Found a slot <3")
		print(f"Found startend tag! {tag}")

	def handle_pi(data, *m):
		print(data)













# class HtclTemplateConfig:
# 	pass

# class HtclTemplate:
# 	def __init__(self, *, config):
# 		pass

# class HtclDocument:
# 	def __init__(self):
# 		pass

# class HtclNode:
# 	name = "Meow"
# 	contents = list
# 	attributes = dict

# 	def __init__(self):
# 		name = "meow"
# 		contents = []
# 		attributes = {}

# 	def is_component(self):

# 		if len(self.name) >= 1:
# 			return self.name[0].isupper()
# 		else:
# 			return False

# 	def create_node():
# 		pass