# -------- Input from User --------

# Take space-separated integers as input and convert to a list
arr = list(map(int, input("Enter array elements separated by space: ").split()))



# Function to perform linear search
def linear_search(arr, target):
    # Loop through each index and element in the array
    for i in range(len(arr)):
        # If the current element matches the target
        if arr[i] == target:
            return i  # Return the index where it's found
    # If loop completes and target not found
    return -1

# -------- Main Program --------

# Example array input
# arr = [5, 12, 7, 20, 9, 14]

# Target element to search for
target = int(input("Enter the element to search: "))

# Call the linear search function
result = linear_search(arr, target)

# Print the result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
