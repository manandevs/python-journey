# Exercise 1: Simple Lambda

# CREATE a lambda function that adds two numbers
add = lambda x, y: x + y

# CALL the lambda function
add_two_number_result = add(3, 7)

# DISPLAY the result
print(add_two_number_result)


# Exercise 2: Square Number

# CREATE a lambda function
Square = lambda x: x * x

# ACCEPT one number
Square_result = Square(3)

# RETURN the square of that number

# DISPLAY the result
print(Square_result)


# Exercise 3: Filter Even Numbers

# CREATE a list of numbers
list_of_number = [1, 2, 3, 4, 5, 6]

# USE a lambda function with filter
is_even = lambda x: x % 2 == 0

# GET only even numbers
even_numbers = list(filter(is_even, list_of_number))

# DISPLAY the result
print(even_numbers)