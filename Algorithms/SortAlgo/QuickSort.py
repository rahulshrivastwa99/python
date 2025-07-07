# Quick Sort function
def quick_sort(arr):
    # Base case: if array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # Choose the last element as pivot
    left = []        # Elements less than pivot
    right = []       # Elements greater than pivot

    # Partition step
    for i in range(len(arr) - 1):  # exclude the pivot
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Recursively sort left and right, and combine
    return quick_sort(left) + [pivot] + quick_sort(right)

# -------- Main Program --------

arr = list(map(int, input("Enter array elements separated by space: ").split()))
print("Sorted array:", quick_sort(arr))
