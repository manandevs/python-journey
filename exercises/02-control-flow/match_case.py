# // Exercise 1: Day Finder

# ASK the user to enter a number from 1 to 7
day_number = int(input("Enter a numver from 1 to 7: "))

# USE match-case
match day_number:
# MATCH each number with the correct day
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# DISPLAY "Invalid day" for an invalid number
    case _:
        print("Invalid day")

# // Exercise 2: Calculator

# ASK the user to enter the first number
first_number = int(input("Enter the first number: "))

# ASK the user to enter an operator
operator = input("Enter an operator: ")

# ASK the user to enter the second number
second_number = int(input("Enter the second number: "))

result = 0

# USE match-case for +, -, *, and /
match operator:
    case "+":
        result = first_number + first_number
    case "-":
        result = first_number - first_number
    case "*":
        result = first_number * first_number
    case "/":
        result = first_number / first_number

# DISPLAY the result
print(first_number , operator,  first_number)
print(result)
