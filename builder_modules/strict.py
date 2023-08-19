import inspect

def strict(function):
    def wrapper(*arguments, **keyword_arguments):
        print("before func")

        signature = inspect.signature(function)

        for iteration, argument in enumerate(arguments):
            # print(signature[iteration])
            print(argument)
        
        for argument in keyword_arguments:
            print(argument)

        function(*arguments, **keyword_arguments)
        print("after function")
    
    return wrapper

@strict
def meow(x: int, y: str, z: float, *, a, b):
    print(x, y)

meow(1, 2, 3.14, a=3, b=4)