# don't worry about these for now :3
import modules.builder as builder
import modules.api as api
import modules.config as config

class BuilderPyExample(builder.Builder):
	pass

import time

# You can specify your compilers with keyword arguments, or override thier functions!
# We have provided a few default values though. If they are too heavy for your liking, feel free
# to edit `modules/builder.py` and remove them!
# BuilderPyExample().blueprint()

# start = time.time_ns()
BuilderPyExample().build_all(0)
# print(f"This took {(time.time_ns() - start) / 1000}mcs or {(time.time_ns() - start) / 1_000_000}ms")