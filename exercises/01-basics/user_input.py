from decimal import Decimal

# A. Financial / Precise Decimal Input
# Example Input: 10.15
price = Decimal(input("Enter item price: $"))
tax = price * Decimal("0.05")

print(f"Tax: ${tax} | Type: {type(tax)}")

# B. Dynamic Mathematical Expressions
# Example Input: 2 * (10 + 5)
expression = input("\nEnter a math problem to solve: ")

# WARNING: eval() executes Python code.
# Only use it with trusted input.
math_result = eval(expression)

print(f"Result: {math_result} | Type: {type(math_result)}")

# Boolean Input
user_confirmation = input(
    "\nDo you want to continue? (yes/no): "
).strip().lower()

is_confirmed = user_confirmation in ("yes", "y", "true", "1")

print(f"Boolean state: {is_confirmed} | Type: {type(is_confirmed)}")

# List, Tuple, and Set Input
# Example Input:
# apple, banana, cherry, apple
raw_input = input("\nEnter items separated by commas: ")

# List (ordered, allows duplicates)
items_list = [item.strip() for item in raw_input.split(",")]
print(f"List: {items_list} | Type: {type(items_list)}")

# Tuple (ordered, immutable)
items_tuple = tuple(items_list)
print(f"Tuple: {items_tuple} | Type: {type(items_tuple)}")

# Set (unordered, removes duplicates)
items_set = set(items_list)
print(f"Set (Unique): {items_set} | Type: {type(items_set)}")

# Multi-line Text Input (Optional)
"""
print(
    "\nEnter your essay block."
    "\nPress Ctrl+D (Linux/macOS)"
    "\nor Ctrl+Z then Enter (Windows) when finished:\n"
)

lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

full_text = "\n".join(lines)

print("\n--- Your Submitted Block ---")
print(full_text)
print(f"Total Characters: {len(full_text)}")
"""

# Integer Validation with Exception Handling
while True:
    try:
        user_age = int(input("\nPlease enter your exact age (whole number): "))

        if user_age < 0 or user_age > 120:
            print("Age must be realistically between 0 and 120.")
            continue

        break

    except ValueError:
        print(
            "Invalid input! "
            "Please enter a whole number only (no letters or decimals)."
        )

print(f"Validated Input Confirmed: {user_age}")