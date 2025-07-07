# Function to perform selection sort
def selection_sort(arr):
    n = len(arr)

    # Loop through the entire array
    for i in range(n):
        min_index = i  # Assume current index is the minimum

        # Find the index of the minimum element
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# -------- Main Program --------
arr = list(map(int, input("Enter array elements separated by space: ").split()))
selection_sort(arr)
print("Sorted array:", arr)
