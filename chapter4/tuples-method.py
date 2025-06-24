# -----------------------------------------
# TUPLE METHODS IN PYTHON — WITH EXAMPLES
# -----------------------------------------

# ✅ Reminder: Tuples are immutable, so they have **only two built-in methods**:
# 1. count()
# 2. index()

# Sample tuple for examples
my_tuple = (10, 20, 30, 20, 40, 50, 20)

# -----------------------------------------
# 1. count(x)
# -----------------------------------------
# ➤ Returns the number of times element x appears in the tuple

print("1. count(x):")
count_20 = my_tuple.count(20)
print("Tuple:", my_tuple)
print("Count of 20:", count_20)  # Output: 3
print()

# -----------------------------------------
# 2. index(x)
# -----------------------------------------
# ➤ Returns the index of the **first occurrence** of element x
# ➤ Raises ValueError if x is not found

print("2. index(x):")
index_30 = my_tuple.index(30)
print("Index of 30:", index_30)  # Output: 2

# Using try-except to safely get index of an element that may not exist
try:
    index_99 = my_tuple.index(99)
except ValueError as e:
    print("Error:", e)
print()

# -----------------------------------------
# Recap in Code Comment
# -----------------------------------------

# ✅ .count(x) → returns how many times x appears
# ✅ .index(x) → returns index of first occurrence of x
# ❌ Tuples do NOT support: append(), remove(), pop(), sort(), etc.
# because they are IMMUTABLE (can't be changed after creation)
