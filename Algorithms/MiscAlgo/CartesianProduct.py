# Take input as list to preserve order
A = input("Enter elements of set A separated by space: ").split()
B = input("Enter elements of set B separated by space: ").split()

# Cartesian product using list comprehension
cartesian_product = [(a, b) for a in A for b in B]

# Print the result
print("\nCartesian Product A × B:")
for pair in cartesian_product:
    print(pair)
