# // Exercise 1: Basic Decorator

# CREATE a decorator function
def my_decorator(func):

# CREATE an inner wrapper function
    def wrapper():

# DISPLAY a message before calling the original function
        print("Message before calling the original function.")

# CALL the original function
        func()

# DISPLAY a message after calling the original function
        print("Message after calling the original function.")

    return wrapper

# // Exercise 2: Apply Decorator

# CREATE a function named 'say_hello'
def say_hello():
     print("Hello, World!")

# APPLY the decorator
decorated_function = my_decorator(say_hello)

# CALL the decorated function
decorated_function()