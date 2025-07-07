# ---------------------------------------------
# ✅ PYTHON LISTS — COMPLETE NOTES WITH COMMENTS
# ---------------------------------------------

# ✅ Lists in Python are:
# - Ordered: Maintain insertion order
# - Mutable: Can be updated
# - Dynamic: Auto-resizable
# - Heterogeneous: Store different types
# - Iterable: You can loop through them

# ---------------------------------------------
# 1. Creating Lists
# ---------------------------------------------
numbers = [10, 20, 30, 40]  # List of integers
names = ["Rahul", "Ankit", "Priya"]  # List of strings
mixed = [1, "Python", 3.14, True]  # List with different data types

print("Numbers:", numbers)
print("Names:", names)
print("Mixed:", mixed)
print()

# ---------------------------------------------
# 2. Indexing and Slicing
# ---------------------------------------------
# Accessing elements by index (0-based)
print("First element:", numbers[0])  # 10
print("Last element:", numbers[-1])  # 40

# Slicing gives a sublist
print("First two:", numbers[:2])     # [10, 20]
print("Last two:", numbers[2:])     # [30, 40]
print()

# ---------------------------------------------
# 3. Lists are Mutable
# ---------------------------------------------
# You can change elements in-place
numbers[1] = 25
print("Changed list:", numbers)  # [10, 25, 30, 40]
print()

# ---------------------------------------------
# 4. Adding Elements
# ---------------------------------------------
numbers.append(50)        # Adds to the end
numbers.insert(1, 15)     # Inserts 15 at index 1
numbers.extend([60, 70])  # Adds multiple items from another list
print("After append, insert, extend:", numbers)
print()

# ---------------------------------------------
# 5. Removing Elements
# ---------------------------------------------
numbers.remove(30)        # Removes first occurrence of 30
numbers.pop()      # Removes last element
numbers.pop(1)   # Removes element at index 1
print("After remove and pop:", numbers)
# print("Popped elements:", last, second)
print()

# ---------------------------------------------
# 6. Membership Test
# ---------------------------------------------
print("Is 25 in list?", 25 in numbers)         # True
print("Is 100 not in list?", 100 not in numbers)  # True
print()

# ---------------------------------------------
# 7. Iterating Over List
# ---------------------------------------------
print("Iterating elements:")
for item in numbers:
    print(item, end=" ")
print("\n")

# ---------------------------------------------
# 8. Sorting and Reversing
# ---------------------------------------------
numbers.sort()        # Sorts in ascending order
print("Sorted list:", numbers)

numbers.reverse()     # Reverses the list
print("Reversed list:", numbers)
print()

# ---------------------------------------------
# 9. Length of List
# ---------------------------------------------
print("Length of list:", len(numbers))  # Count of elements
print()

# ---------------------------------------------
# 10. Copying a List
# ---------------------------------------------
copy_list = numbers.copy()  # Makes a shallow copy
print("Copied list:", copy_list)
print()

# ---------------------------------------------
# 11. List Comprehension
# ---------------------------------------------
# Short way to create a list from a loop
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)  # [1, 4, 9, 16, 25]
print()

# ---------------------------------------------
# 12. Nested Lists (2D Lists)
# ---------------------------------------------
matrix = [[1, 2], [3, 4], [5, 6]]
print("Matrix:", matrix)
print("Element at 2nd row, 1st column:", matrix[1][0])  # 3
print()

# ---------------------------------------------
# 13. More List Methods
# ---------------------------------------------
my_list = [10, 20, 30, 40, 20]

# index(x): returns index of first x
print("Index of 30:", my_list.index(30))

# count(x): returns number of times x occurs
print("Count of 20:", my_list.count(20))

# clear(): removes all elements
temp = [1, 2, 3]
temp.clear()
print("After clear():", temp)

# reverse(): reverses the list in-place
rev = [1, 2, 3]
rev.reverse()
print("Reversed list:", rev)

# copy(): creates a copy of list
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print("Original:", original)
print("Copied (after append):", copied)
print()

# ---------------------------------------------
# 📊 14. Time Complexity Summary (Important)
# ---------------------------------------------
print("List Operations and Time Complexity:")
print("""
Access by index        → O(1)
Append to end          → O(1) amortized
Insert/remove in middle→ O(n)
Search (in keyword)    → O(n)
Copy/slice             → O(n)
Sort                   → O(n log n)
Reverse                → O(n)
""")
