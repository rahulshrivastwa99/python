# -------- Input from User --------

# Take space-separated integers as input and convert to a list
arr = list(map(int, input("Enter sorted array elements separated by space: ").split()))

# Ask user for the target element to search
target = int(input("Enter the element to search: "))

# -------- Binary Search Function --------

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Loop while search space is valid
    while low <= high:
        mid = (low + high) // 2  # Find middle index

        if arr[mid] == target:
            return mid           # Found target, return index
        elif arr[mid] < target:
            low = mid + 1        # Search in right half
        else:
            high = mid - 1       # Search in left half

    return -1  # Target not found

# -------- Call and Output --------

# Call the function
result = binary_search(arr, target)

# Print result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
