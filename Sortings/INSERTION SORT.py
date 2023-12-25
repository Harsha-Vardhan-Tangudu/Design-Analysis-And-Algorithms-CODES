# Import necessary libraries
import random
import time
import psutil

# Function to perform insertion sort with counting comparisons and swaps
def insertion_sort(arr, comparisons, swaps):
    primitive_operations = 0  # Initialize a counter for primitive operations
    
    for j in range(1, len(arr)):  # Outer loop runs n-1 times, where n is the length of the array - O(n)
        primitive_operations += 1  # Increment operation count for j
        key = arr[j]  # Constant time (Θ(1)) - 1 assignment operation
        primitive_operations += 1  # Increment operation count for key assignment
        i = j - 1  # Constant time (Θ(1)) - 1 assignment operation
        primitive_operations += 1  # Increment operation count for i assignment
        
        while i >= 0 and arr[i] > key:  # Inner loop runs until i >= 0 and arr[i] > key
            primitive_operations += 1  # Increment operation count for the while condition
            
            comparisons[0] += 1  # Increment comparisons count (O(1) operation) - 1 operation
            primitive_operations += 1  # Increment operation count for comparisons[0] assignment
            
            arr[i + 1] = arr[i]  # Shifting an element to the right - O(1) operation
            primitive_operations += 1  # Increment operation count for arr[i + 1] assignment
            swaps[0] += 1  # Increment swaps count (O(1) operation) - 1 operation
            primitive_operations += 1  # Increment operation count for swaps[0] assignment
            
            i -= 1  # Decrementing i - Constant time (Θ(1)) - 1 operation
            primitive_operations += 1  # Increment operation count for i decrement
        
        arr[i + 1] = key  # Placing the key in its correct position - O(1) operation
        primitive_operations += 1  # Increment operation count for arr[i + 1] assignment
    
    return primitive_operations  # Return the total count of primitive operations

# Function to generate a random array of a given size
def generate_random_array(size):
    primitive_operations = 0  # Initialize a counter for primitive operations
    arr = []  # Initialize an empty array
    
    for _ in range(size):  # Loop runs 'size' times - O(size) operations
        primitive_operations += 1  # Increment operation count for the loop
        rand_num = random.randint(1, 100000)  # Generate a random number - O(1) operation
        primitive_operations += 1  # Increment operation count for rand_num assignment
        arr.append(rand_num)  # Append the random number to the array - O(1) operation
        primitive_operations += 1  # Increment operation count for arr.append
        
    return arr, primitive_operations  # Return the generated array and the total count of primitive operations

# Function to generate a sorted array in the best-case scenario
def generate_best_case_array(size):
    primitive_operations = 0  # Initialize a counter for primitive operations
    arr = []  # Initialize an empty array
    
    for i in range(1, size + 1):  # Loop runs 'size' times - O(size) operations
        primitive_operations += 1  # Increment operation count for the loop
        arr.append(i)  # Append the value to the array - O(1) operation
        primitive_operations += 1  # Increment operation count for arr.append
        
    return arr, primitive_operations  # Return the generated array and the total count of primitive operations

# Function to generate an inverted array in the worst-case scenario
def generate_worst_case_array(size):
    primitive_operations = 0  # Initialize a counter for primitive operations
    arr = []  # Initialize an empty array
    
    for i in range(size, 0, -1):  # Loop runs 'size' times - O(size) operations
        primitive_operations += 1  # Increment operation count for the loop
        arr.append(i)  # Append the value to the array - O(1) operation
        primitive_operations += 1  # Increment operation count for arr.append
        
    return arr, primitive_operations  # Return the generated array and the total count of primitive operations

# Sizes for test cases
test_sizes = [100, 500, 1000]

for size in test_sizes:
    # Generate random input test case
    random_array, random_primitive_operations = generate_random_array(size)  # O(size) operations
    
    # Display the input test case
    print(f"Input Test Case (Size {size}):")
    print(random_array)

    # Initialize counters for comparisons and swaps
    comparisons = [0]
    swaps = [0]

    # Measure running time
    start_time = time.time()  # Start time measurement - O(1)

    # Perform Insertion Sort with counting
    total_primitive_operations = insertion_sort(random_array, comparisons, swaps)  # Overall time complexity: O(n^2)
    
    # Calculate running time in milliseconds
    end_time = time.time()  # End time measurement - O(1)
    running_time_ms = (end_time - start_time) * 1000  # Calculate running time in milliseconds - O(1)

    # Calculate memory usage
    memory_used_bytes = psutil.Process().memory_info().rss  # Memory usage measurement - O(1)

    # Display the sorted array, metrics, and memory usage for the current test case
    print("\nSorted Array:")
    print(random_array)
    print("Number of comparisons (Θ(n^2)): O(n^2):", comparisons[0])  # Comparisons count - O(1)
    print("Number of swaps (Θ(n^2)): O(n^2):", swaps[0])  # Swaps count - O(1)
    print("Running time (milliseconds):", running_time_ms)  # Running time - O(1)
    print("Memory used (bytes):", memory_used_bytes)  # Memory usage - O(1)
    print("Total primitive operations:", total_primitive_operations)  # Total primitive operations - O(1)
    print("\n" + "=" * 40 + "\n")

    # Generate best-case input test case
    best_case_array, best_case_primitive_operations = generate_best_case_array(size)  # O(size) operations

    # Display the best-case input test case
    print(f"Best-case Input Test Case (Size {size}):")
    print(best_case_array)

    # Reset counters for comparisons and swaps
    comparisons = [0]
    swaps = [0]

    # Measure running time for best-case scenario
    start_time = time.time()  # Start time measurement - O(1)

    # Perform Insertion Sort with counting for best-case scenario
    total_primitive_operations = insertion_sort(best_case_array, comparisons, swaps)  # Overall time complexity: O(n)

    # Calculate running time in milliseconds for best-case scenario
    end_time = time.time()  # End time measurement - O(1)
    running_time_ms = (end_time - start_time) * 1000  # Calculate running time in milliseconds - O(1)

    # Calculate memory usage for best-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss  # Memory usage measurement - O(1)

    # Display the sorted array, metrics, and memory usage for the best-case scenario
    print("\nSorted Array (Best-case):")
    print(best_case_array)
    print("Number of comparisons (Θ(n)): O(n):", comparisons[0])  # Comparisons count - O(1)
    print("Number of swaps (Θ(n)): O(n):", swaps[0])  # Swaps count - O(1)
    print("Running time (milliseconds):", running_time_ms)  # Running time - O(1)
    print("Memory used (bytes):", memory_used_bytes)  # Memory usage - O(1)
    print("Total primitive operations:", total_primitive_operations)  # Total primitive operations - O(1)
    print("\n" + "=" * 40 + "\n")

    # Generate worst-case input test case
    worst_case_array, worst_case_primitive_operations = generate_worst_case_array(size)  # O(size) operations

    # Display the worst-case input test case
    print(f"Worst-case Input Test Case (Size {size}):")
    print(worst_case_array)

    # Reset counters for comparisons and swaps
    comparisons = [0]
    swaps = [0]

    # Measure running time for worst-case scenario
    start_time = time.time()  # Start time measurement - O(1)

    # Perform Insertion Sort with counting for worst-case scenario
    total_primitive_operations = insertion_sort(worst_case_array, comparisons, swaps)  # Overall time complexity: O(n^2)

    # Calculate running time in milliseconds for worst-case scenario
    end_time = time.time()  # End time measurement - O(1)
    running_time_ms = (end_time - start_time) * 1000  # Calculate running time in milliseconds - O(1)

    # Calculate memory usage for worst-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss  # Memory usage measurement - O(1)

    # Display the sorted array, metrics, and memory usage for the worst-case scenario
    print("\nSorted Array (Worst-case):")
    print(worst_case_array)
    print("Number of comparisons (Θ(n^2)): O(n^2):", comparisons[0])  # Comparisons count - O(1)
    print("Number of swaps (Θ(n^2)): O(n^2):", swaps[0])  # Swaps count - O(1)
    print("Total primitive operations:", total_primitive_operations)  # Total primitive operations - O(1)
    print("Running time (milliseconds):", running_time_ms)  # Running time - O(1)
    print("Memory used (bytes):", memory_used_bytes)  # Memory usage - O(1)
    print("\n" + "=" * 40 + "\n")
