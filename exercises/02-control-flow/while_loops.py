
import random

# // Exercise 1: Print Numbers

# CREATE 'number' AND SET TO 1
number = 1

# CREATE a while loop
# CONTINUE while number is less than or equal to 10
while number <= 10:

# DISPLAY number
    print(number)

# INCREASE number by 1
    number += 1


# // Exercise 2: Password Checker

# CREATE 'correct_password' AND SET TO "python123"
correct_password = "python123"

# ASK the user to enter a password
password = input("Enter a password: ")

# CONTINUE asking while the password is incorrect
while password != correct_password:
    print("Incorrect! Try again.")
    password = input("Enter a password: ")

# DISPLAY "Access granted" when correct
print("Access granted")


# // Exercise 3: Number Guessing Game

# CREATE 'secret_number'
secret_number = random.randint(1, 100)

# ASK the user to guess the number
guess = int(input("Guess the number (1-100): "))

# CONTINUE asking until the guess is correct
while secret_number != guess:
    # Add helpful hints so the user can actually solve it
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
        
    guess = int(input("Guess again: "))

# DISPLAY a success message
print("Congratulations! You guessed the secret number!")