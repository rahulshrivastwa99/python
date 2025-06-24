# ---------------------------------------------------------
# ✅ CONDITIONAL STATEMENTS IN PYTHON — FULL NOTES + CODE
# ---------------------------------------------------------

# ▶️ What are Conditional Statements?
# Conditional statements help a program **make decisions** based on conditions (True/False).
# These are also called **decision control statements**.

# ---------------------------------------
# ✅ TYPES OF CONDITIONAL STATEMENTS
# ---------------------------------------
# 1. if
# 2. if-else
# 3. if-elif-else
# 4. nested if
# 5. one-line (ternary operator)
# 6. logical operators (and, or, not)

# ---------------------------------------------------------
# 1️⃣ if Statement — Executes block only if condition is True
# ---------------------------------------------------------

print("🔹 Example 1: if statement")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("Not Eligible")# ✅ This line will execute
print()

# ---------------------------------------------------------
# 2️⃣ if-else Statement — One block runs, the other is skipped
# ---------------------------------------------------------

print("🔹 Example 2: if-else")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")
print()

# ---------------------------------------------------------
# 3️⃣ if-elif-else — Multiple conditions, first match executes
# ---------------------------------------------------------

print("🔹 Example 3: if-elif-else")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
print()

# ---------------------------------------------------------
# 4️⃣ Nested if — if inside another if
# ---------------------------------------------------------

print("🔹 Example 4: Nested if")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "rahul":
    if password == "1234":
        print("Login successful.")
    else:
        print("Wrong password.")
else:
    print("Unknown username.")
print()

# ---------------------------------------------------------
# 5️⃣ Logical Operators (and, or, not)
# ---------------------------------------------------------

print("🔹 Example 5: Logical Operators")

age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote.")
else:
    print("Not eligible.")

# OR operator
is_student = False
has_id = True

if is_student or has_id:
    print("Entry allowed (student or ID verified).")
print()

# NOT operator
logged_in = False
if not logged_in:
    print("Please log in to continue.")
print()

# ---------------------------------------------------------
# 6️⃣ Ternary Operator — Short if-else in one line
# ---------------------------------------------------------

print("🔹 Example 6: Ternary Operator")

age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print("You are:", status)
print()

# ---------------------------------------------------------
# ✅ Comparison Operators Used in Conditions
# ---------------------------------------------------------
# ==  → Equal to
# !=  → Not equal to
# >   → Greater than
# <   → Less than
# >=  → Greater than or equal to
# <=  → Less than or equal to

# ---------------------------------------------------------
# ✅ Logical Operators Summary
# ---------------------------------------------------------
# and → True if both conditions are True
# or  → True if at least one condition is True
# not → Reverses the condition (True → False, False → True)

# ---------------------------------------------------------
# ✅ Use Cases of Conditional Statements
# ---------------------------------------------------------
# - Login systems
# - Form validations
# - Game conditions (win/lose)
# - Menu-based applications
# - Automated decisions (like grading, access, permissions)

# ---------------------------------------------------------
# ✅ Tips
# ---------------------------------------------------------
# ✅ Use proper indentation (4 spaces) in if blocks
# ✅ Use elif instead of multiple ifs when conditions are related
# ✅ Use logical operators for combining multiple conditions
# ✅ Use nested if only when necessary

