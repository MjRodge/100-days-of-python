# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrap(*args, **kwargs):
        print(f"function executed {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrap


# Use the decorator 👇
@logging_decorator
def my_function(a, b, c):
    return a+b+c


my_function(1, 2, 3)
