# // Exercise: Login System

# CREATE 'correct_username' AND SET TO "admin"
correct_username = "admin"

# CREATE 'correct_password' AND SET TO "1234"
correct_password = "1234"

# ASK the user to enter a username
username = input("Enter username: ")

# IF the username is correct
if username == correct_username:
    # ASK the user to enter a password
    password = input("Enter password: ")

    # IF the password is correct
    # DISPLAY "Login successful"
    if password == correct_password:
        print("Login successful")

    # OTHERWISE
    # DISPLAY "Incorrect password"
    else:
        print("Incorrect password")

# OTHERWISE
# DISPLAY "Incorrect username"
else:
    print("Incorrect username")



# // Exercise: Positive Number Check

# ASK the user to enter a number
number = int(input("Enter a number: "))

# IF the number is greater than 0
if number > 0:

    # IF the number is divisible by 2
    # DISPLAY "Positive and Even"
    if number%2 == 0:
        print("Positive and Even")

    # OTHERWISE
    # DISPLAY "Positive and Odd"
    else: 
        print("Psitive and Odd")
# OTHERWISE
# DISPLAY "Number is not positive"
else:
    print("Number is not positive")