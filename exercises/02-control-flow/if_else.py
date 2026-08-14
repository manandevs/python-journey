# // Exercise 1: Voting Eligibility

# ASK the user to enter their age
age = int(input("Enter their age: "))

# IF age is greater than or equal to 18
# DISPLAY "You can vote"
if age > 18:
    print("You can vot")

# OTHERWISE
# DISPLAY "You cannot vote"
else: 
    print("You cannot vote")

# // Exercise 2: Even or Odd

# ASK the user to enter a number
number = int(input("Enter a number: "))

# IF the number is divisible by 2
# DISPLAY "Even"
if number % 2 ==0: 
    print("Even")

# OTHERWISE
# DISPLAY "Odd"
else:
    print("ODD")


# // Exercise 3: Grade System

# ASK the user to enter marks
marks = int(input("Enter your marks: "))

# IF marks are 80 or greater
# DISPLAY "A"
if marks > 80: 
    print("A Grage")

# OTHERWISE IF marks are 70 or greater
# DISPLAY "B"
elif marks > 70: 
    print("B Grage")

# OTHERWISE IF marks are 60 or greater
# DISPLAY "C"
elif marks > 60: 
    print("C Grage")

# OTHERWISE
# DISPLAY "Fail"
else: 
    print("Fail")