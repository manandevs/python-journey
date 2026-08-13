# PYTHON DATA TYPES EXAMPLES

# // Integer
# CREATE 'score' AND SET TO 100
# score = 100  # OR
score = int(100)

# DISPLAY VALUE
print("score =", score)

# DISPLAY TYPE
print("Type:", type(score))
print()


# // Float (Decimal)
# CREATE 'price' AND SET TO 19.99
# price = 19.99  # OR
price = float(19.99)

# DISPLAY VALUE
print("price =", price)

# DISPLAY TYPE
print("Type:", type(price))
print()


# // Boolean
# CREATE 'is_logged_in' AND SET TO TRUE
# is_logged_in = True  # OR
is_logged_in = bool(True)

# DISPLAY VALUE
print("is_logged_in =", is_logged_in)

# DISPLAY TYPE
print("Type:", type(is_logged_in))
print()


# // String
# CREATE 'name' AND SET TO "Alice"
# name = "Alice"  # OR
name = str("Alice")

# DISPLAY VALUE
print("name =", name)

# DISPLAY TYPE
print("Type:", type(name))
print()


# // List (Array)
# CREATE 'fruits' AND STORE ["apple", "banana", "cherry"]
# fruits = ["apple", "banana", "cherry"]  # OR
fruits = list(("apple", "banana", "cherry"))

# DISPLAY VALUE
print("fruits =", fruits)

# DISPLAY TYPE
print("Type:", type(fruits))
print()


# // Tuple
# CREATE 'coordinates' AND STORE (10, 20)
# coordinates = (10, 20)  # OR
coordinates = tuple((10, 20))

# DISPLAY VALUE
print("coordinates =", coordinates)

# DISPLAY TYPE
print("Type:", type(coordinates))
print()


# // Set
# CREATE 'colors' AND STORE {"red", "green", "blue"}
# colors = {"red", "green", "blue"}  # OR
colors = set(("red", "green", "blue"))

# DISPLAY VALUE
print("colors =", colors)

# DISPLAY TYPE
print("Type:", type(colors))
print()


# // Dictionary
# CREATE 'student' WITH name AND age
# student = {"name": "Alice", "age": 20}  # OR
student = dict(name="Alice", age=20)

# DISPLAY VALUE
print("student =", student)

# DISPLAY TYPE
print("Type:", type(student))
print()


# // Complex Number
# CREATE 'number' AND SET TO 2 + 3j
# number = 2 + 3j  # OR
number = complex(2, 3)

# DISPLAY VALUE
print("number =", number)

# DISPLAY TYPE
print("Type:", type(number))
print()

number2 = 2 + 3j
print(type(number2))
print()


# // NoneType
# CREATE 'result' AND SET TO NONE
# result = None
result = None

# DISPLAY VALUE
print("result =", result)

# DISPLAY TYPE
print("Type:", type(result))