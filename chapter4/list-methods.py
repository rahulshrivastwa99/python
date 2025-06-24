# -----------------------------------------------
# PYTHON LIST METHODS - EXAMPLES WITH NOTES
# -----------------------------------------------

# We’ll explore: append(), insert(), extend(), remove(), pop(), clear(),
# index(), count(), sort(), reverse(), copy()

# Sample list
my_list = [10, 20, 30, 40, 20]

# 1. append(x)
# ------------------
# Adds an element at the end of the list
print("1. append(x):")
my_list.append(50)
print("After append(50):", my_list)
print()

# 2. insert(i, x)
# ------------------
# Inserts element x at index i (shifts remaining elements to the right)
print("2. insert(i, x):")
my_list.insert(2, 25)  # Insert 25 at index 2
print("After insert(2, 25):", my_list)
print()

# 3. extend(iterable)
# ------------------
# Adds all elements of an iterable (e.g. list, tuple) to the end
print("3. extend(iterable):")
my_list.extend([60, 70])
print("After extend([60, 70]):", my_list)
print()

# 4. remove(x)
# ------------------
# Removes the **first occurrence** of x
print("4. remove(x):")
my_list.remove(20)  # Only the first 20 is removed
print("After remove(20):", my_list)
print()

# 5. pop([i])
# ------------------
# Removes and returns the element at index i (default: last)
print("5. pop():")
last_item = my_list.pop()
print("After pop():", my_list)
print("Popped item:", last_item)

second_item = my_list.pop(1)
print("After pop(1):", my_list)
print("Popped item at index 1:", second_item)
print()

# 6. clear()
# ------------------
# Removes all elements from the list
print("6. clear():")
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear():", temp_list)
print()

# 7. index(x)
# ------------------
# Returns the index of the **first** occurrence of x
print("7. index(x):")
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
print()

# 8. count(x)
# ------------------
# Returns the number of times x appears in the list
print("8. count(x):")
count_of_20 = [10, 20, 20, 30].count(20)
print("Count of 20:", count_of_20)
print()

# 9. sort()
# ------------------
# Sorts the list in ascending order (modifies in-place)
print("9. sort():")
unsorted_list = [5, 1, 8, 3]
unsorted_list.sort()
print("Sorted list:", unsorted_list)

# Optional: sort descending
unsorted_list.sort(reverse=True)
print("Sorted descending:", unsorted_list)
print()

# 10. reverse()
# ------------------
# Reverses the elements in place (not sorted reverse, just flip order)
print("10. reverse():")
rev_list = [1, 2, 3]
rev_list.reverse()
print("Reversed list:", rev_list)
print()

# 11. copy()
# ------------------
# Returns a shallow copy of the list
print("11. copy():")
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)
print("Original list:", original)
print("Copied list (after append):", copy_list)
