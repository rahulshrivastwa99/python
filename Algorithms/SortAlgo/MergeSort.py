# Merge Sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    # Step 1: Divide the array
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Merge the sorted halves
    return merge(left_half, right_half)

# Helper function to merge two sorted arrays
def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from left and right, and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements from left and right (if any)
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

# -------- Main Program --------

arr = list(map(int, input("Enter array elements separated by space: ").split()))
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
