import modules.log as log

# This looks funky so lemmie explain.
# This is a decorator, that returns a normal decorator. This lets
# us take paramaters to the decorator. Make sense?
# Yes... unfortuntely this nesting is needed...
def expect(exception: str) -> any:
	"""
	A decorator that takes an argument that will print if the function fails,
	used to avoid heavy nesting caused by try-except statements in public
	python APIs.

	Returns the type from the decorated function, or a string if it raised an
	exception. (I would use `any | str` but cpython don't like that very much)

	This is best used in the most limited context possible, as you can basically
	consider the function it is used on to be an unsafe block*.

	\* No it won't call them all the way up the stack lik regular try-except blocks,
	but its still best to avoid them for blocks you know are safe.
	"""
	def decorator(function):
		def wrapper(*args, **kwargs):
			try:
				result = function(*args, **kwargs)
			except:
				log.error(exception)
				result = exception
			return result
		return wrapper
	return decorator