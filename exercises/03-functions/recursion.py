# Exercise 1: Countdown

# CREATE a recursive function named 'countdown'
def countdown(n):
    if n < 0:
        return
    else:
        print(n)
        countdown(n - 1)


# ACCEPT a number
countdown_number = int(input("Enter a number for countdown: "))

# CALL the function to display the countdown
countdown(countdown_number)


# Exercise 2: Factorial

# CREATE a recursive function named 'factorial'
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# ACCEPT a number
factorial_number = int(input("Enter a number for factorial: "))

# CALCULATE the factorial
factorial_result = factorial(factorial_number)

# DISPLAY the result
print(f"The factorial of {factorial_number} is {factorial_result}")