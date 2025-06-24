# -----------------------------------------------------
# ✅ FUNCTIONS IN PYTHON — FULL NOTES + EXAMPLES IN CODE
# -----------------------------------------------------

# ▶️ What is a Function?
# A function is a block of code that performs a specific task.
# It avoids code repetition and helps in modular programming.

# -----------------------------------------------------
# 1️⃣ Basic Function Definition and Calling
# -----------------------------------------------------

def greet():
    print("Hello, welcome to Python functions!")

greet()  # Calling the function
greet()  # Calling the function
greet()  # Calling the function

# -----------------------------------------------------
# 2️⃣ Function with Parameters and Arguments
# -----------------------------------------------------

def greet_user(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet_user("Rahul")  # "Rahul" is an argument

# -----------------------------------------------------
# 3️⃣ Function with Return Value
# -----------------------------------------------------

def add(a, b):
    return a + b  # Returns the result to the caller

result = add(5, 3)
print("Sum is:", result)

# -----------------------------------------------------
# 4️⃣ Default Parameter Values
# -----------------------------------------------------

def greet_country(country="India"):
    print(f"Greetings from {country}")

greet_country()         # Uses default
greet_country("Nepal")  # Overrides default

# -----------------------------------------------------
# 5️⃣ Keyword Arguments
# -----------------------------------------------------

def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=21, name="Sourav")  # Order doesn't matter

# -----------------------------------------------------
# 6️⃣ *args — Variable Number of Positional Arguments
# -----------------------------------------------------

def total_sum(*numbers):
    print("Numbers received:", numbers)
    print("Sum =", sum(numbers))

total_sum(10, 20, 30, 40)  # Passed as tuple

# -----------------------------------------------------
# 7️⃣ **kwargs — Variable Number of Keyword Arguments
# -----------------------------------------------------

def print_profile(**details):
    print("Profile details:")
    for key, value in details.items():
        print(f"{key}: {value}")

print_profile(name="Suraj", age=22, course="B.Tech")

# -----------------------------------------------------
# 8️⃣ Recursive Function (calls itself)
# -----------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))

# -----------------------------------------------------
# 9️⃣ Lambda (Anonymous) Function
# -----------------------------------------------------

square = lambda x: x * x
print("Square of 4 is:", square(4))

# Can also be used with `map`, `filter`, `reduce`

# -----------------------------------------------------
# 🔟 Function Scope — Local vs Global Variables
# -----------------------------------------------------

x = 10  # Global variable

def show():
    x = 5  # Local variable
    print("Inside function:", x)

show()
print("Outside function:", x)

# -----------------------------------------------------
# ✅ Best Practices for Functions:
# -----------------------------------------------------
# - Function names should be lowercase_with_underscores
# - Keep functions short and specific
# - Use docstrings for documentation
# - Return values instead of printing inside functions (for reusability)
# - Avoid using global variables unless necessary

# -----------------------------------------------------
# ✅ Summary:
# -----------------------------------------------------
# def my_function():         → define a function
# my_function()              → call a function
# parameters → input names in function definition
# arguments  → actual values you pass
# return     → sends result back to the caller
# *args      → collects extra positional arguments as tuple
# **kwargs   → collects extra keyword arguments as dict
# lambda     → short one-line function

