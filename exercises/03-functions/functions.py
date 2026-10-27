# // Exercise 1: Create a Function

# CREATE a function named 'greet'
def greet():

# DISPLAY "Hello, World!" inside the function
    print("Hello, World!")

# CALL the function
greet()


# // Exercise 2: Multiple Calls

# CREATE a function named 'welcome'
def welcome():

# DISPLAY a welcome message
    print("Welcome")

# CALL the function three times

for _ in range(0,3):
    welcome()

# // Exercise 3: Calculator Function

# CREATE a function that adds two numbers
def add_numbers(a, b):

# DISPLAY the result
    print(a+b)

# CALL the function

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

add_numbers(number1, number2)