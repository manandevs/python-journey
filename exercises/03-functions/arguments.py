# // Exercise 1: Function Arguments

# CREATE a function named 'greet'
# ADD a parameter named 'name'
def greet(name):

# DISPLAY "Hello" followed by name
    print(f"Hello, {name}")

# CALL the function with different names
greet("Marless")
greet("Alex")
greet("Jordan")

# // Exercise 2: Multiple Arguments

# CREATE a function named 'add_numbers'

# ACCEPT two arguments
def add_numbers(a, b):

# ADD them together
    add = a + b

# DISPLAY the result
    print(add)

add_numbers(1,2)


# // Exercise 3: Default Argument

# CREATE a function with a default value
def greet_user(name="Guest"):
    print(f"Welcome back, {name}!")

# CALL the function without providing the argument
greet_user()

# CALL the function with providing the argument
greet_user("Marless")