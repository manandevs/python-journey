# // Variable stored as text
# CREATE 'age_str' AND SET TO "20" 
age_str = "20"
print("Original String Value:", age_str)
print("Data Type Checking:", type(age_str))
print()

# // Convert text to integer to allow math operations
# CREATE 'age_num' AND SET TO CONVERT_TO_INTEGER(age_str)
age_num = int(age_str)  # Fixed: assigned to age_num instead of overwriting age_str
print("Converted to Integer:", age_num)
print("Data Type Checking:", type(age_num))
print()

# CREATE 'next_year' AND SET TO age_num + 1
next_year = age_num + 1  # Fixed: used age_num instead of age_str

# DISPLAY "Next year you will be: " combined with CONVERT_TO_STRING(next_year)
print("Next year you will be: " + str(next_year))  # Fixed: converted to string for concatenation
print("Data Type Checking:", type(next_year))
print()


# 1. IMPLICIT TYPE CONVERSION (Automatic)
print(" 1. Implicit Conversion ")
print()

an_int = 5
a_float = 2.5

# Python automatically promotes the integer to a float to prevent data loss
implicit_result = an_int + a_float
print(f"Result: {implicit_result} | Type: {type(implicit_result)}") 
print()

# Python automatically converts boolean True to 1 during math operations
bool_math = True + 10 
print(f"Bool Math Result: {bool_math} | Type: {type(bool_math)}\n")
print()

# 2. EXPLICIT TYPE CASTING (Manual)
print(" 2. Explicit Type Casting ")
print()

# A. String to Integer / Float
price_str = "49.99"
quantity_str = "3"

price_float = float(price_str)          # "49.99" -> 49.99
quantity_int = int(quantity_str)        # "3" -> 3

total_cost = price_float * quantity_int
print(f"Total Cost: {total_cost} | Type: {type(total_cost)}")
print()

# B. Float to Integer (Truncation / Lossy Conversion)
# Notice that int() truncates the decimal; it does NOT round up.
pi_float = 3.99
pi_int = int(pi_float)
print(f"Float {pi_float} cast to Int: {pi_int}")
print()

# C. Number to String (For Concatenation)
score = 100
message = "Your high score is: " + str(score)
print(message)
print()

# D. Boolean Casting (Evaluating Truthiness)
# 0, empty strings, and empty collections become False. Everything else is True.
print(f"Is empty string True? {bool('')}")
print(f"Is number 5 True? {bool(5)}\n")
print()

# 3. COLLECTION TYPE CASTING
print(" 3. Collection Casting ")

# Start with a list containing duplicate values
raw_list = [10, 20, 20, 30, 10, 40]
print("Original List:", raw_list)
print()

# Cast List to Set to instantly strip out all duplicates
unique_set = set(raw_list)
print("Cast to Set (Duplicates Removed):", unique_set)
print()

# Cast Set back to List so it can be indexed again
clean_list = list(unique_set)
print("Cast back to List:", clean_list)
print()

# Cast List to an Immutable Tuple
final_tuple = tuple(clean_list)
print("Cast to Tuple:", final_tuple)
print()
