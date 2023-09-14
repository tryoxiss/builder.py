from builder_modules.core import expect

@expect("I mad ea mistakey wakey uwu")
def meow():
	if 1 == "b":
		print("WHAT??")
		return 1

# Errors on pourpose
@expect("I made a mistake ;c")
def hiss():
	if client.hiss == 2:
		return 1

@expect("I hiss after purring!")
def purr():
	print("Purr ...")
	hiss()
	print("Hiss!")


print(meow())
meow()

print(hiss())
hiss()

print(purr())
purr()