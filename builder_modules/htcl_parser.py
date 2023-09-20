import html.parser as LemmieViewItsSource
import builder_modules.core_classes as classes

from builder_modules.html_parser import HTMLParser as HtmlParser
import builder_modules.log as log

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

	# Procesing Instructions, I know its a bad name.
	def handle_pi(self, data):
		print(f"Found a processing instruction: {data}")

		if data.startswith("py"):
			handle_py_block(strip_processing_instruction(data))

def strip_processing_instruction(data):
	return data.lstrip("py").rstrip("/py?").lstrip(" ").rstrip(" ").rstrip("/n").lstrip("/n")

def handle_py_block(code: str):
	print(code)

	log.warning("handle_py_block blindly executes code contained within, make sure you check the code yourself!")
	
	# try:
	exec(f"""
import builder_modules.api as api

{code}""")
	# except:
		# log.error(f"Invalid code: {code}")

def _handle_component():
	pass