# Function to perform insertion sort
def insertion_sort(arr):
    n = len(arr)

    # Start from the second element
    for i in range(1, n):
        key = arr[i]      # Current element to insert
        j = i - 1

        # Shift elements of the sorted part to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
 # While sort in decreasing order:-
        # while j >= 0 and arr[j] < key:
        #     arr[j+1] = arr[j]
        #     j-= 1

        # Insert the key at its correct position
        arr[j + 1] = key

# -------- Main Program --------

arr = list(map(int, input("Enter array elements separated by space: ").split()))
insertion_sort(arr)
print("Sorted array:", arr)
