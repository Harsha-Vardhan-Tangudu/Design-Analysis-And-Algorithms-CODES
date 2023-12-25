def max_crossing_sum(arr, low, mid, high):
    # Initialize left_sum and right_sum to negative infinity
    left_sum = float('-inf')
    right_sum = float('-inf')
    
    # Find the maximum sum on the left side of the mid-point
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
    
    # Find the maximum sum on the right side of the mid-point
    sum = 0
    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
    
    # Return the maximum sum that crosses the mid-point
    return left_sum + right_sum

def max_subarray_sum(arr, low, high):
    # Base case: If there's only one element, return it
    if low == high:
        return arr[low]

    # Calculate the middle index
    mid = (low + high) // 2

    # Recursively find the maximum subarray sum on the left and right sides
    left_max = max_subarray_sum(arr, low, mid)
    right_max = max_subarray_sum(arr, mid + 1, high)

    # Find the maximum subarray sum that crosses the midpoint
    cross_max = max_crossing_sum(arr, low, mid, high)

    # Return the maximum of the three sums
    return max(left_max, right_max, cross_max)

# Driver code
if __name__ == '__main__':
    arr = [2, -3, 4, -1, -2, 1, 5, -3]
    max_sum = max_subarray_sum(arr, 0, len(arr) - 1)
    print("Maximum subarray sum is:", max_sum)