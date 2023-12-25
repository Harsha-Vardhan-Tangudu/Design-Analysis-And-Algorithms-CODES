import random
import time
import psutil

# Function to perform insertion sort with counting comparisons and swaps
def insertion_sort(bucket, comparisons, swaps, primitive_operations):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
            comparisons[0] += 1  # Increment comparisons count
            swaps[0] += 1  # Increment swaps count
            primitive_operations[0] += 3  # Increment primitive operations count (comparison, swap, and assignment)
        bucket[j + 1] = key
        swaps[0] += 1  # Increment swaps count
        primitive_operations[0] += 1  # Increment primitive operations count (assignment)

# Function to perform bucket sort with counting comparisons and swaps
def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        n = 1  # Ensure at least one bucket in case of an empty input array
    max_value = max(arr)
    B = [[] for _ in range(n)]
    comparisons = [0]  # Counter for comparisons
    swaps = [0]  # Counter for swaps
    primitive_operations = [0]  # Counter for primitive operations

    for i in range(n):
        index = int((n - 1) * arr[i] / max_value)
        B[index].append(arr[i])

    for i in range(n):
        insertion_sort(B[i], comparisons, swaps, primitive_operations)

    sorted_array = []
    for bucket in B:
        sorted_array.extend(bucket)

    primitive_operations[0] += len(arr)  # Adding the initial assignment of values to buckets

    return sorted_array, comparisons[0], swaps[0], primitive_operations[0]

# Function to generate a random array of a given size
def generate_random_array(size):
    return [random.uniform(0, 1) for _ in range(size)]

# Function to generate a sorted array in the best-case scenario
def generate_best_case_array(size):
    return [i / size for i in range(size)]

# Function to generate a reverse-sorted array in the worst-case scenario
def generate_worst_case_array(size):
    return [i / size for i in range(size, 0, -1)]

# Sizes for test cases
test_sizes = [100, 500, 1000]

for size in test_sizes:
    # Generate random input test case
    random_array = generate_random_array(size)
    
    # Display the input test case
    print(f"Input Test Case (Size {size}):")
    print(random_array)

    # Measure running time
    start_time = time.time()

    # Perform Bucket Sort with counting
    sorted_arr, comparisons, swaps, primitive_operations = bucket_sort(random_array)

    # Calculate running time in milliseconds
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the current test case
    print("\nSorted Array:")
    print(sorted_arr)
    print("Number of comparisons:", comparisons)
    print("Number of swaps:", swaps)
    print("Number of primitive operations:", primitive_operations)
    print("Running time (milliseconds):", running_time_ms)
    print("Memory used (bytes):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")

    # Generate best-case input test case
    best_case_array = generate_best_case_array(size)
    
    # Measure running time for best-case scenario
    start_time = time.time()

    # Perform Bucket Sort with counting for best-case scenario
    sorted_arr, comparisons, swaps, primitive_operations = bucket_sort(best_case_array)

    # Calculate running time in milliseconds for best-case scenario
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage for best-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the best-case scenario
    print(f"Best-case Input Test Case (Size {size}):")
    print(best_case_array)
    print("Sorted Array (Best-case):")
    print(sorted_arr)
    print("Number of comparisons (Best-case):", comparisons)
    print("Number of swaps (Best-case):", swaps)
    print("Number of primitive operations (Best-case):", primitive_operations)
    print("Running time (milliseconds, Best-case):", running_time_ms)
    print("Memory used (bytes, Best-case):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")

    # Generate worst-case input test case
    worst_case_array = generate_worst_case_array(size)
    
    # Measure running time for worst-case scenario
    start_time = time.time()

    # Perform Bucket Sort with counting for worst-case scenario
    sorted_arr, comparisons, swaps, primitive_operations = bucket_sort(worst_case_array)

    # Calculate running time in milliseconds for worst-case scenario
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage for worst-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the worst-case scenario
    print(f"Worst-case Input Test Case (Size {size}):")
    print(worst_case_array)
    print("Sorted Array (Worst-case):")
    print(sorted_arr)
    print("Number of comparisons (Worst-case):", comparisons)
    print("Number of swaps (Worst-case):", swaps)
    print("Number of primitive operations (Worst-case):", primitive_operations)
    print("Running time (milliseconds, Worst-case):", running_time_ms)
    print("Memory used (bytes, Worst-case):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")
