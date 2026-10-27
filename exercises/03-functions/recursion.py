# Exercise 1: Countdown

# CREATE a recursive function named 'countdown'
def countdown(n):
    if n <= 0:
        return
    else:
        print(n)
        countdown(n - 1)

# ACCEPT a number
countdown_number = int(input("Enter a number: "))

countdown_results = countdown(countdown_number)

# DISPLAY the number
print(countdown_results)

# CALL the function again with the number decreased by 1

# STOP when the number reaches 0

# // Exercise 2: Factorial

# CREATE a recursive function

# CALCULATE the factorial of a number

# DISPLAY the result