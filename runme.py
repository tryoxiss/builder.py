# don't worry about these for now :3
import modules.builder as builder
import modules.api as api
import modules.config as config

class BuilderPyExample(builder.Builder):
	pass

# You can specify your compilers with keyword arguments, or override thier functions!
# We have provided a few default values though. If they are too heavy for your liking, feel free
# to edit `modules/builder.py` and remove them!
# BuilderPyExample().blueprint()

builder.Builder().build_all(config.content.directory, 0)