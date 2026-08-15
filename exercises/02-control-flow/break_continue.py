import random
# // Exercise 1: Print Numbers

# CREATE 'number' AND SET TO 1
number = 1

# CREATE a while loop
# CONTINUE while number is less than or equal to 10
while True:

# DISPLAY number
    print(number)

# INCREASE number by 1
    number += 1

 # If the condition is met, skip the rest and go to the next loop cycle
    if number <= 10:
        continue
        
    # If the condition is met, exit the loop entirely
    if number > 10:
        break


# // Exercise 2: Password Checker

# CREATE 'correct_password' AND SET TO "python123"
correct_password = "python123"

# ASK the user to enter a password
password = input("Enter a password: ")

# CONTINUE asking while the password is incorrect
while True:
    if password != correct_password:
        password = input("Enter a password: ")
        continue

# DISPLAY "Access granted" when correct
    else:
        print("Access granted")
        break

# // Exercise 3: Number Guessing Game
import random  # Required to use random.randint

# CREATE 'secret_number'
secret_number = random.randint(1, 1000)

# CONTINUE asking until the guess is correct
while True:
    # ASK the user to guess the number and convert to an integer
    guess_number = int(input("Guess the number (1-1000): "))

    # Check if the guess is incorrect
    if guess_number != secret_number:

        # Fixed logic: If guess is bigger than secret, it's too high!
        if guess_number > secret_number:
            print("Too high")
        else:
            print("Too small")

        # Automatically loops back up to the top
        continue

    # DISPLAY a success message
    else:
        print("Success! You guessed the correct number!")
        break