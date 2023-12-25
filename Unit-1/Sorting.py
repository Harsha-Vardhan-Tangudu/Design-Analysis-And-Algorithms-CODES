
#Keep dividing the array into two halves until each sublist consists of a single element. Merge the sorted sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted array
def merge_sort(arr):
    if len(arr) > 1:
        # Calculate the middle index of the array
        mid = len(arr) // 2

        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0  # Initialize pointers for left_half, right_half, and arr

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


#Choose a pivot element and partition the array such that all elements to the left of the pivot are smaller than the pivot and all elements to the right of the pivot are greater than the pivot. Recursively sort the left and right sublists
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # Choose the first element as the pivot
    left = []
    right = []
    equal = []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            right.append(element)

    # Recursively sort the left and right sublists
    left = quick_sort(left)
    right = quick_sort(right)

    return left + equal + right


#consider leftmost element as pivot; partition the array such that all elements to the left of the pivot are smaller than the pivot and all elements to the right of the pivot are greater than the pivot
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position in the sorted array
        arr[j + 1] = key

    return arr


#Find the minimum element in the unsorted part of the array and swap it with the first element of the unsorted part of the array
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        # Find the index of the minimum element in the unsorted part of the array
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted part of the array
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


#Divide the range of array elements into buckets and then sort each bucket individually using Tim sort
def bucket_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Create buckets
    bucket_count = max_element // 10 + 1
    buckets = [[] for _ in range(bucket_count)]

    # Add elements into the buckets
    for element in arr:
        buckets[element // 10].append(element)

    # Sort the elements of each bucket
    for i in range(bucket_count):
        buckets[i].sort()

    # Concatenate all the sorted buckets
    k = 0
    for i in range(bucket_count):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

    return arr


def heapify(arr, n, i):
    # Find the largest element among the root node and its children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap the root node if it is not the largest element
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the new root node to ensure it's the largest
        heapify(arr, n, largest)


#Build a max-heap from the array and then repeatedly swap the root node with the last node of the heap and heapify the root node
def heap_sort(arr):
    # Build a max-heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

    # Heap sort
    for i in range(len(arr) - 1, 0, -1):
        # Swap the root node (maximum element) of the heap with the last element of the heap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify the root node
        heapify(arr, i, 0)

    return arr

    
# Driver code
if __name__ == '__main__':
    arr = [2, -3, 4, -1, -2, 1, 5, -3]
    print("Sorted array using merge sort:", merge_sort(arr))

    arr = [2, -3, 4, -1, -2, 1, 5, -3]
    print("Sorted array using quick sort:", quick_sort(arr))

    arr = [2, -3, 4, -1, -2, 1, 5, -3]
    print("Sorted array using insertion sort:", insertion_sort(arr))

    arr = [2, -3, 4, -1, -2, 1, 5, -3]
    print("Sorted array using selection sort:", selection_sort(arr))

    arr = [2, -3, 4, -1, -2, 1, 5, -3]
    print("Sorted array using bucket sort:", bucket_sort(arr))

    arr = [2, -3, 4, -1, -2, 1, 5, -3]
    print("Sorted array using heap sort:", heap_sort(arr))