# don't worry about these for now :3
import modules.builder as builder
import modules.api as api

class BuilderPyExample(builder.Builder):
	pass

# You can specify your compilers with keyword arguments, or override thier functions!
# We have provided a few default values though. If they are too heavy for your liking, feel free
# to edit `modules/builder.py` and remove them!
BuilderPyExample().blueprint()



# file = builder.File("content/lyrics.txt")

# print(file.content)
# print(file.name())
# print(file.path)

import modules.file as wut

a = wut.BuilderFile("lyrics.txt")

print(a.content)
print(a.path)