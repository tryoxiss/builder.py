class Compiler:
	def compile(string: str):
		print("Compiled :sparkles: (not really)")


class Test:
	name = "none"

	def __init__(self, template_engine=Compiler()):
		self.name == "purr"
		self.template_engine = template_engine

	def get_name(self):
		print(self.name)
	
	def handle_template(self):
		self.template_engine.compile()
	
	def run(self):
		print("Running!")

class Meow(Test):
	def get_name(self):
		print("no")


Meow().run()

# meow = Meow()

# meow.get_name()
# meow.handle_template()