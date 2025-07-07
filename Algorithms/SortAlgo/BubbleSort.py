# Function to perform bubble sort
def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop runs n-1 times
    for i in range(n):
        # Inner loop compares adjacent elements
        for j in range(n - i - 1):
            # If current element is greater than next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            
    # if sort in decreasing order:-
            # if arr[j] < arr[j + 1]:
            #      arr[j], arr[j + 1] = arr[j + 1], arr[j]


# -------- Main Program --------

# Take array input from user
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Call bubble sort function
bubble_sort(arr)

# Print sorted array
print("Sorted array:", arr)
