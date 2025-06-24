# -------------------------------------------
# TUPLES IN PYTHON — NOTES + CODE EXAMPLES
# -------------------------------------------

# ✅ What is a Tuple?
# A tuple is an ordered, immutable (unchangeable) collection of items.
# It can hold elements of different data types (heterogeneous).
# Tuples are written with round brackets: ()

# -------------------------------------------
# 1. Creating Tuples
# -------------------------------------------

print("1. Creating Tuples:")

empty = ()                         # Empty tuple
single = (10,)                     # Single element tuple (comma is required!)
multi = (1, 2, 3, 4)
mixed = (1, "hello", 3.14, True)

print("Empty tuple:", empty)
print("Single element tuple:", single)
print("Multiple items:", multi)
print("Mixed types:", mixed)
print()

# -------------------------------------------
# 2. Accessing Elements (Indexing and Slicing)
# -------------------------------------------

print("2. Accessing Elements:")

print("First item:", multi[0])         # Indexing starts from 0
print("Last item:", multi[-1])         # Negative indexing
print("Slice [1:3]:", multi[1:3])      # Slicing (does NOT include end index)
print()

# -------------------------------------------
# 3. Tuple is Immutable (can't modify)
# -------------------------------------------

print("3. Immutability:")

try:
    multi[1] = 100                     # Error! Tuples can't be modified
except TypeError as e:
    print("Error when trying to modify tuple:", e)
print()

# -------------------------------------------
# 4. Looping through a Tuple
# -------------------------------------------

print("4. Looping through Tuple:")
for item in mixed:
    print(item, end=" ")
print("\n")

# -------------------------------------------
# 5. Tuple Unpacking
# -------------------------------------------

print("5. Tuple Unpacking:")

point = (4, 5)
x, y = point                          # Unpacks values into variables
print("x =", x)
print("y =", y)
print()

# -------------------------------------------
# 6. Tuple Methods
# -------------------------------------------

print("6. Tuple Methods:")

sample = (10, 20, 30, 20, 40)

print("Count of 20:", sample.count(20))       # How many times 20 appears
print("Index of 30:", sample.index(30))       # First index of 30
print()

# -------------------------------------------
# 7. Nested Tuples (Tuple inside tuple)
# -------------------------------------------

print("7. Nested Tuples:")

nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("Access nested item:", nested[1][0])    # Accessing 3
print()

# -------------------------------------------
# 8. Tuple vs List Summary
# -------------------------------------------

print("8. Tuple vs List:")

# Tuples use (), Lists use []
# Tuples are immutable, Lists are mutable

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print("Before changing list:", my_list)
my_list[0] = 10
print("After changing list:", my_list)

print("Tuple remains unchanged:", my_tuple)
print()
