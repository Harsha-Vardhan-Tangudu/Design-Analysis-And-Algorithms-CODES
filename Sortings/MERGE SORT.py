import random
import time
import psutil

# Function to perform merge sort with counting comparisons, swaps, and other primitive operations
def merge_sort(arr, low, high, comparisons, swaps, primitive_operations):
    if low < high:
        middle = (low + high) // 2  # Constant time (Θ(1))
        merge_sort(arr, low, middle, comparisons, swaps, primitive_operations)  # T(n/2)
        merge_sort(arr, middle + 1, high, comparisons, swaps, primitive_operations)  # T(n/2)
        merge(arr, low, middle, high, comparisons, swaps, primitive_operations)  # O(n)

# Function to merge two subarrays during merge sort
def merge(arr, low, middle, high, comparisons, swaps, primitive_operations):
    left = arr[low:middle + 1]  # Creating left subarray - O(n)
    right = arr[middle + 1:high + 1]  # Creating right subarray - O(n)

    i, j, k = 0, 0, low  # Initializing indices - Constant time (Θ(1))

    while i < len(left) and j < len(right):  # Loop runs until one subarray is exhausted - O(n)
        comparisons[0] += 1  # Increment comparisons count (O(1) operation)
        if left[i] <= right[j]:  # Comparison - O(1)
            arr[k] = left[i]  # Copy operation - O(1)
            i += 1
        else:
            arr[k] = right[j]  # Copy operation - O(1)
            j += 1
            swaps[0] += 1  # Increment swaps count (O(1) operation)
        k += 1
        primitive_operations[0] += 3  # Increment primitive operations count (3 assignments)

    while i < len(left):  # Copy remaining elements of left subarray - O(n)
        arr[k] = left[i]
        i += 1
        k += 1
        primitive_operations[0] += 2  # Increment primitive operations count (2 assignments)

    while j < len(right):  # Copy remaining elements of right subarray - O(n)
        arr[k] = right[j]
        j += 1
        k += 1
        primitive_operations[0] += 2  # Increment primitive operations count (2 assignments)

# Function to generate a random array of a given size
def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]  # Generating random numbers - O(n)

# Function to generate a sorted array in the best-case scenario
def generate_best_case_array(size):
    return list(range(1, size + 1))  # Creating a sorted array - O(n)

# Function to generate a reverse-sorted array in the worst-case scenario
def generate_worst_case_array(size):
    return list(range(size, 0, -1))  # Creating a reverse-sorted array - O(n)

# Sizes for test cases
test_sizes = [100, 500, 1000]

for size in test_sizes:
    # Generate random input test case
    random_array = generate_random_array(size)  # O(n)
    
    # Display the input test case
    print(f"Input Test Case (Size {size}):")
    print(random_array)

    # Initialize counters for comparisons, swaps, and primitive operations
    comparisons = [0]
    swaps = [0]
    primitive_operations = [0]

    # Measure running time
    start_time = time.time()  # Start time measurement - O(1)

    # Perform Merge Sort with counting
    merge_sort(random_array, 0, size - 1, comparisons, swaps, primitive_operations)  # Overall time complexity: T(n) = 2T(n/2) + O(n) => O(n log n)

    # Calculate running time in milliseconds
    end_time = time.time()  # End time measurement - O(1)
    running_time_ms = (end_time - start_time) * 1000  # Calculate running time in milliseconds - O(1)

    # Calculate memory usage
    memory_used_bytes = psutil.Process().memory_info().rss  # Memory usage measurement - O(1)

    # Display the sorted array, metrics, and memory usage for the current test case
    print("\nSorted Array:")
    print(random_array)
    print("Number of comparisons (Θ(n log n)): O(n log n):", comparisons[0])  # Comparisons count - O(1)
    print("Number of swaps (Θ(n log n)): O(n log n):", swaps[0])  # Swaps count - O(1)
    print("Number of primitive operations:", primitive_operations[0])  # Primitive operations count - O(1)
    print("Running time (milliseconds):", running_time_ms)  # Running time - O(1)
    print("Memory used (bytes):", memory_used_bytes)  # Memory usage - O(1)
    print("\n" + "=" * 40 + "\n")

    # Generate best-case input test case
    best_case_array = generate_best_case_array(size)  # O(n)

    # Display the best-case input test case
    print(f"Best-case Input Test Case (Size {size}):")
    print(best_case_array)

    # Reset counters for comparisons, swaps, and primitive operations
    comparisons = [0]
    swaps = [0]
    primitive_operations = [0]

    # Measure running time for best-case scenario
    start_time = time.time()  # Start time measurement - O(1)

    # Perform Merge Sort with counting for best-case scenario
    merge_sort(best_case_array, 0, size - 1, comparisons, swaps, primitive_operations)  # Overall time complexity: T(n) = 2T(n/2) + O(n) => O(n log n)

    # Calculate running time in milliseconds for best-case scenario
    end_time = time.time()  # End time measurement - O(1)
    running_time_ms = (end_time - start_time) * 1000  # Calculate running time in milliseconds - O(1)

    # Calculate memory usage for best-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss  # Memory usage measurement - O(1)

    # Display the sorted array, metrics, and memory usage for the best-case scenario
    print("\nSorted Array (Best-case):")
    print(best_case_array)
    print("Number of comparisons (Θ(n log n)): O(n log n):", comparisons[0])  # Comparisons count - O(1)
    print("Number of swaps (Θ(n log n)): O(n log n):", swaps[0])  # Swaps count - O(1)
    print("Number of primitive operations:", primitive_operations[0])  # Primitive operations count - O(1)
    print("Running time (milliseconds):", running_time_ms)  # Running time - O(1)
    print("Memory used (bytes):", memory_used_bytes)  # Memory usage - O(1)
    print("\n" + "=" * 40 + "\n")

    # Generate worst-case input test case
    worst_case_array = generate_worst_case_array(size)  # O(n)

    # Display the worst-case input test case
    print(f"Worst-case Input Test Case (Size {size}):")
    print(worst_case_array)

    # Reset counters for comparisons, swaps, and primitive operations
    comparisons = [0]
    swaps = [0]
    primitive_operations = [0]

    # Measure running time for worst-case scenario
    start_time = time.time()  # Start time measurement - O(1)

    # Perform Merge Sort with counting for worst-case scenario
    merge_sort(worst_case_array, 0, size - 1, comparisons, swaps, primitive_operations)  # Overall time complexity: T(n) = 2T(n/2) + O(n) => O(n log n)

    # Calculate running time in milliseconds for worst-case scenario
    end_time = time.time()  # End time measurement - O(1)
    running_time_ms = (end_time - start_time) * 1000  # Calculate running time in milliseconds - O(1)

    # Calculate memory usage for worst-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss  # Memory usage measurement - O(1)

    # Display the sorted array, metrics, and memory usage for the worst-case scenario
    print("\nSorted Array (Worst-case):")
    print(worst_case_array)
    print("Number of comparisons (Θ(n log n)): O(n log n):", comparisons[0])  # Comparisons count - O(1)
    print("Number of swaps (Θ(n log n)): O(n log n):", swaps[0])  # Swaps count - O(1)
    print("Number of primitive operations:", primitive_operations[0])  # Primitive operations count - O(1)
    print("Running time (milliseconds):", running_time_ms)  # Running time - O(1)
    print("Memory used (bytes):", memory_used_bytes)  # Memory usage - O(1)
    print("\n" + "=" * 40 + "\n")
