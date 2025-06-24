# ----------------------------------------------------
# ✅ COMPLETE SET NOTES IN PYTHON (With CODE & EXAMPLES)
# ----------------------------------------------------

# ▶ What is a Set?
# A set is an **unordered**, **unindexed**, **mutable** collection of **unique elements**.
# Sets are useful when you want to store non-duplicate values and perform operations like union, intersection, etc.

# ✅ Set Properties:
# ----------------------------
# 1. ✅ Unordered — no indexing, no guaranteed order
# 2. ✅ Mutable — you can add/remove elements
# 3. ✅ Unique — duplicates are automatically removed
# 4. ❌ No indexing or slicing allowed
# 5. ✅ Iterable — can loop through sets

# -----------------------------------------
# 1. Creating Sets
# -----------------------------------------

print("1️⃣ Creating Sets")

empty_set = set()  # Use set(), not {} — {} creates a dictionary
fruits = {"apple", "banana", "mango", "banana"}  # Duplicate 'banana' is removed
print("Empty Set:", empty_set)
print("Fruits Set:", fruits)
print()

# -----------------------------------------
# 2. Adding Elements
# -----------------------------------------

print("2️⃣ Adding Elements")

fruits.add("orange")  # Add single item
print("After add('orange'):", fruits)

fruits.update(["grape", "apple", "kiwi"])  # Add multiple items
print("After update([...]):", fruits)
print()

# -----------------------------------------
# 3. Removing Elements
# -----------------------------------------

print("3️⃣ Removing Elements")

fruits.remove("apple")  # Removes item; error if not present
print("After remove('apple'):", fruits)

fruits.discard("banana")  # Removes item; NO error if not present
fruits.discard("pear")    # No error even if 'pear' is not in set
print("After discard('banana', 'pear'):", fruits)

removed_item = fruits.pop()  # Removes random element (sets are unordered)
print("Removed item with pop():", removed_item)
print("Set now:", fruits)

fruits.clear()  # Remove all elements
print("After clear():", fruits)
print()

# -----------------------------------------
# 4. Set Operations (Union, Intersection, etc.)
# -----------------------------------------

print("4️⃣ Set Operations")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)
print("B:", B)

print("Union (A | B):", A | B)                  # or A.union(B)
print("Intersection (A & B):", A & B)          # or A.intersection(B)
print("Difference (A - B):", A - B)            # Only in A
print("Symmetric Difference (A ^ B):", A ^ B)  # Items in A or B but not both
print()

# -----------------------------------------
# 5. Membership Test
# -----------------------------------------

print("5️⃣ Membership Test")

print("Is 2 in A?", 2 in A)
print("Is 5 not in A?", 5 not in A)
print()

# -----------------------------------------
# 6. Looping Through a Set
# -----------------------------------------

print("6️⃣ Looping Through Set")

for item in A:
    print(item, end=" ")
print("\n")

# -----------------------------------------
# 7. Real-Life Use Case: Remove Duplicates from List
# -----------------------------------------

print("7️⃣ Real-Life Use Case")

names_list = ["Rahul", "Ankit", "Rahul", "Priya", "Ankit"]
unique_names = set(names_list)  # Convert to set to remove duplicates
print("Original List:", names_list)
print("Unique Names:", unique_names)
print()

# -----------------------------------------
# 8. Set Methods (Quick Examples)
# -----------------------------------------

print("8️⃣ Common Set Methods")

s = {10, 20, 30}
print("Original set:", s)

s.add(40)                    # Add item
s.update([50, 60])          # Add multiple items
s.discard(10)               # Remove item safely
print("After add/update/discard:", s)

s2 = {50, 60, 70}
print("Intersection:", s.intersection(s2))
print("Union:", s.union(s2))
print("Difference:", s.difference(s2))
print("Symmetric Difference:", s.symmetric_difference(s2))
print()

# -----------------------------------------
# 9. Summary (in comments)
# -----------------------------------------

# ✅ Common Set Methods:
# - add(x)                   → Add element
# - update(iterable)         → Add multiple elements
# - remove(x)                → Remove element (error if not present)
# - discard(x)               → Remove element (no error if not present)
# - pop()                    → Remove random element
# - clear()                  → Empty the set
# - union(set2)              → All unique elements from both
# - intersection(set2)       → Common elements
# - difference(set2)         → Elements only in first set
# - symmetric_difference()   → Elements in either, but not both

# ✅ Use Cases:
# - Remove duplicates from list
# - Fast membership checking
# - Performing math set operations (A ∪ B, A ∩ B, etc.)
