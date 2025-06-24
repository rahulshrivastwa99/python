# ---------------------------------------------
# LISTS IN PYTHON — CODE WITH FEATURES/NOTES
# ---------------------------------------------

# ✅ Python lists are:
# - Ordered (they maintain the order of insertion)
# - Mutable (you can change, add, or delete elements)
# - Heterogeneous (can contain elements of different types)
# - Dynamic (grow or shrink as needed)
# - Iterable (can be looped over)

# ---------------------------------------------
# 1. Creating a List
# ---------------------------------------------
numbers = [10, 20, 30, 40]  # List of integers
names = ["Rahul", "Ankit", "Priya"]  # List of strings
mixed = [1, "Python", 3.14, True]    # Heterogeneous list

print("1. Original Lists:")
print("Numbers:", numbers)
print("Names:", names)
print("Mixed types allowed:", mixed)
print()

# ---------------------------------------------
# 2. Indexing (positive and negative)
# ---------------------------------------------
print("2. Indexing:")
print("First element:", numbers[0])     # Accessing by positive index
print("Last element:", numbers[-1])     # Accessing by negative index
print()

# ---------------------------------------------
# 3. Slicing
# ---------------------------------------------
print("3. Slicing:")
print("First 2 elements:", numbers[:2])     # Slice from start to index 2 (excluded)
print("Last 2 elements:", numbers[-2:])     # Slice using negative indices
print()

# ---------------------------------------------
# 4. Lists are Mutable (you can change values)
# ---------------------------------------------
print("4. Mutability:")
numbers[1] = 25          # Change second element (20 → 25)
print("After change:", numbers)
print()

# ---------------------------------------------
# 5. Adding Elements (append, insert)
# ---------------------------------------------
print("5. Adding Elements:")
numbers.append(50)       # Adds to end
numbers.insert(1, 15)    # Inserts 15 at index 1
print("After append and insert:", numbers)
print()

# ---------------------------------------------
# 6. Removing Elements (remove, pop)
# ---------------------------------------------
print("6. Removing Elements:")
numbers.remove(30)       # Removes first occurrence of 30
last = numbers.pop()     # Removes and returns last element
print("After remove and pop:", numbers)
print("Popped item:", last)
print()

# ---------------------------------------------
# 7. Membership Test (in / not in)
# ---------------------------------------------
print("7. Membership Test:")
print("Is 25 in list?", 25 in numbers)
print("Is 100 not in list?", 100 not in numbers)
print()

# ---------------------------------------------
# 8. Iterating (Lists are Iterable)
# ---------------------------------------------
print("8. Iteration:")
for item in numbers:
    print(item, end=" ")
print("\n")

# ---------------------------------------------
# 9. Sorting and Reversing (in-place)
# ---------------------------------------------
print("9. Sort and Reverse:")
numbers.sort()            # Sorts in ascending order
print("Sorted:", numbers)

numbers.reverse()         # Reverses current order
print("Reversed:", numbers)
print()

# ---------------------------------------------
# 10. Length of List
# ---------------------------------------------
print("10. Length:")
print("List length:", len(numbers))   # Counts all elements
print()

# ---------------------------------------------
# 11. Copying a List
# ---------------------------------------------
print("11. Copying:")
copy_of_numbers = numbers.copy()  # Creates a shallow copy
print("Copied list:", copy_of_numbers)
print()

# ---------------------------------------------
# 12. List Comprehension (one-line loop)
# ---------------------------------------------
print("12. List Comprehension:")
squares = [x*x for x in range(1, 6)]  # Creates list of squares from 1 to 5
print("Squares:", squares)
print()

# ---------------------------------------------
# 13. Nested Lists (Lists within a list)
# ---------------------------------------------
print("13. Nested Lists:")
matrix = [[1, 2], [3, 4], [5, 6]]  # 2D list like a matrix
print("Matrix:", matrix)
print("Element at 2nd row, 1st col:", matrix[1][0])  # Accessing nested elements
