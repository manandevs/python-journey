# Exercise 1: Local Variable

# CREATE a function
def local_variable():

    # CREATE a variable inside the function
    variable_inside = "I am a local variable"

    # DISPLAY the variable inside the function
    print(variable_inside)


# CALL the function
local_variable()

# TRY accessing it outside the function
# print(variable_inside)


# // Exercise 2: Global Variable

# CREATE a variable outside a function
variable_global = "I am a global variable"

# ACCESS the variable inside a function
def global_variable():
    print(variable_global)

# DISPLAY the value
global_variable()

# Exercise 3: Modify Global Variable

# CREATE a global variable
variable_modify_global = "I am a modify global variable"

# MODIFY it inside a function using the global keyword
def modify_global():
    global variable_modify_global
    variable_modify_global = "I have been modified!"

# CALL the function
modify_global()

# DISPLAY the updated value
print(variable_modify_global)