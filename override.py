class Compiler:
	def compile(self, string: str):
		print("Compiled :sparkles: (not really)")

class AltCompiler:
	def compile(self, string: str):
		print("Compiling with alternate compiler")

class Test:
	name = "none"

	def __init__(self, template_engine=Compiler()):
		self.name == "purr"
		self.template_engine = template_engine

	def get_name(self):
		print(self.name)
	
	def handle_template(self):
		self.template_engine.compile("kitteh")
	
	def run(self):
		print("Running!")
	
	def test(self):
		print("Wow!");

class Meow(Test):
	def get_name(self):
		print("no")
		self.test()


# Meow(template_engine=Compiler()).handle_template()

# Meow(template_engine=AltCompiler()).handle_template()

meow = Meow()

meow.get_name()
meow.handle_template()