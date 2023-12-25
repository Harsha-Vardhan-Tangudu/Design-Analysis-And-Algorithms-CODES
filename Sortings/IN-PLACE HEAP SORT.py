import random
import time
import psutil

# Function to perform MAX_HEAPIFY with counting comparisons and swaps
def MAX_HEAPIFY(A, i, heap_size, comparisons, swaps, primitive_operations):
    left = 2 * i
    right = 2 * i + 1
    largest = i

    if left <= heap_size:
        comparisons[0] += 1  # Increment comparisons count (O(1) operation)
        primitive_operations[0] += 1  # Increment primitive operations count
        if A[left - 1] > A[largest - 1]:
            largest = left

    if right <= heap_size:
        comparisons[0] += 1  # Increment comparisons count (O(1) operation)
        primitive_operations[0] += 1  # Increment primitive operations count
        if A[right - 1] > A[largest - 1]:
            largest = right

    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        swaps[0] += 1  # Increment swaps count (O(1) operation)
        primitive_operations[0] += 3  # Increment primitive operations count by 3 (two assignments and a swap)
        MAX_HEAPIFY(A, largest, heap_size, comparisons, swaps, primitive_operations)

# Function to build a max heap with counting comparisons and swaps
def BUILD_MAX_HEAP(A, comparisons, swaps, primitive_operations):
    heap_size = len(A)
    for i in range(heap_size // 2, 0, -1):
        MAX_HEAPIFY(A, i, heap_size, comparisons, swaps, primitive_operations)

# Function to perform inplace heap sort with counting comparisons and swaps
def inplace_heapsort(A, comparisons, swaps, primitive_operations):
    BUILD_MAX_HEAP(A, comparisons, swaps, primitive_operations)
    heap_size = len(A)
    for i in range(heap_size, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        swaps[0] += 1  # Increment swaps count (O(1) operation)
        primitive_operations[0] += 3  # Increment primitive operations count by 3 (two assignments and a swap)
        heap_size -= 1
        MAX_HEAPIFY(A, 1, heap_size, comparisons, swaps, primitive_operations)

# Function to generate a random array of a given size
def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]

# Function to generate a sorted array in the best-case scenario
def generate_best_case_array(size):
    return list(range(1, size + 1))

# Function to generate a reverse-sorted array in the worst-case scenario
def generate_worst_case_array(size):
    return list(range(size, 0, -1))

# Sizes for test cases
test_sizes = [100, 500, 1000]

for size in test_sizes:
    # Generate random input test case
    random_array = generate_random_array(size)
    
    # Display the input test case
    print(f"Input Test Case (Size {size}):")
    print(random_array)

    # Initialize counters for comparisons, swaps, and primitive operations
    comparisons = [0]
    swaps = [0]
    primitive_operations = [0]

    # Measure running time
    start_time = time.time()

    # Perform Inplace Heap Sort with counting
    inplace_heapsort(random_array, comparisons, swaps, primitive_operations)  # Overall time complexity: O(n log n)

    # Calculate running time in milliseconds
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the current test case
    print("\nSorted Array:")
    print(random_array)
    print("Number of comparisons (Θ(n log n)): O(n log n):", comparisons[0])
    print("Number of swaps (Θ(n log n)): O(n log n):", swaps[0])
    print("Number of primitive operations:", primitive_operations[0])
    print("Running time (milliseconds):", running_time_ms)
    print("Memory used (bytes):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")

    # Generate best-case input test case
    best_case_array = generate_best_case_array(size)

    # Display the best-case input test case
    print(f"Best-case Input Test Case (Size {size}):")
    print(best_case_array)

    # Reset counters for comparisons, swaps, and primitive operations
    comparisons = [0]
    swaps = [0]
    primitive_operations = [0]

    # Measure running time for best-case scenario
    start_time = time.time()

    # Perform Inplace Heap Sort with counting for best-case scenario
    inplace_heapsort(best_case_array, comparisons, swaps, primitive_operations)  # Overall time complexity: O(n log n)

    # Calculate running time in milliseconds for best-case scenario
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage for best-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the best-case scenario
    print("\nSorted Array (Best-case):")
    print(best_case_array)
    print("Number of comparisons (Θ(n log n)): O(n log n):", comparisons[0])
    print("Number of swaps (Θ(n log n)): O(n log n):", swaps[0])
    print("Number of primitive operations:", primitive_operations[0])
    print("Running time (milliseconds):", running_time_ms)
    print("Memory used (bytes):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")

    # Generate worst-case input test case
    worst_case_array = generate_worst_case_array(size)

    # Display the worst-case input test case
    print(f"Worst-case Input Test Case (Size {size}):")
    print(worst_case_array)

    # Reset counters for comparisons, swaps, and primitive operations
    comparisons = [0]
    swaps = [0]
    primitive_operations = [0]

    # Measure running time for worst-case scenario
    start_time = time.time()

    # Perform Inplace Heap Sort with counting for worst-case scenario
    inplace_heapsort(worst_case_array, comparisons, swaps, primitive_operations)  # Overall time complexity: O(n log n)

    # Calculate running time in milliseconds for worst-case scenario
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage for worst-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the worst-case scenario
    print("\nSorted Array (Worst-case):")
    print(worst_case_array)
    print("Number of comparisons (Θ(n log n)): O(n log n):", comparisons[0])
    print("Number of swaps (Θ(n log n)): O(n log n):", swaps[0])
    print("Number of primitive operations:", primitive_operations[0])
    print("Running time (milliseconds):", running_time_ms)
    print("Memory used (bytes):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")
