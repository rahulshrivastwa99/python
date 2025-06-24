# -------------------------------------
# TYPECASTING IN PYTHON (with Examples)
# -------------------------------------

# Typecasting means converting one data type into another.
# Two types of casting:
# 1. Implicit Typecasting – Python automatically converts types
# 2. Explicit Typecasting – Programmer manually converts types

# -------------------------------------
# 1. IMPLICIT TYPECASTING
# -------------------------------------

print("Implicit Typecasting:")
x = 5          # Integer
y = 2.0        # Float
z = x + y      # Python automatically converts int (x) to float

print("x (int):", x, "| type:", type(x))
print("y (float):", y, "| type:", type(y))
print("z = x + y (auto converted to float):", z, "| type:", type(z))
print()

# Why? Because adding int + float needs both to be float for accurate math.

# -------------------------------------
# 2. EXPLICIT TYPECASTING
# -------------------------------------
# This is done manually using built-in functions like int(), float(), str(), etc.

print("Explicit Typecasting:")

# a. STRING to INTEGER
a = "123"
b = int(a)  # Converts numeric string to integer
print("String '123' to int:", b, "| type:", type(b))

# b. FLOAT to INTEGER
f = 10.9
g = int(f)  # Truncates decimal part, does NOT round
print("Float 10.9 to int:", g, "| type:", type(g))
print()

# c. STRING to FLOAT
h = "15.5"
i = float(h)  # Converts numeric string with decimal to float
print("String '15.5' to float:", i, "| type:", type(i))

# d. INTEGER to FLOAT
j = 7
k = float(j)  # Simple conversion from int to float
print("Int 7 to float:", k, "| type:", type(k))
print()

# e. INTEGER/FLOAT to STRING
m = 100
n = str(m)  # Converts int to string
print("Int 100 to string:", n, "| type:", type(n))

p = 99.99
q = str(p)  # Converts float to string
print("Float 99.99 to string:", q, "| type:", type(q))
print()

# f. VALUES to BOOLEAN
# bool() returns False for:
# - zero (0)
# - empty structures (like '', [], {})
# - None
# Everything else is True

print("Bool Typecasting:")
print("bool(0):", bool(0))         # False (0 is considered False)
print("bool(1):", bool(1))         # True
print("bool(-10):", bool(-10))     # True (any non-zero number is True)
print("bool(''):", bool(""))       # False (empty string)
print("bool('Python'):", bool("Python"))  # True (non-empty string)
print()

# g. COLLECTION TYPECASTING

print("Collection Typecasting:")

# String to list – breaks string into list of characters
s = "hello"
print("list('hello'):", list(s))   # ['h', 'e', 'l', 'l', 'o']

# Tuple to list – just converts type
t = (1, 2, 3)
print("list((1,2,3)):", list(t))   # [1, 2, 3]

# List to tuple – changes list into tuple
l = [4, 5, 6]
print("tuple([4,5,6]):", tuple(l)) # (4, 5, 6)

# List to set – removes duplicates and converts to unordered set
dupes = [1, 2, 2, 3]
print("set([1,2,2,3]):", set(dupes))  # {1, 2, 3}
