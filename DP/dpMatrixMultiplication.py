import sys

def matrix_chain_multiplication_order(dimensions):
    n = len(dimensions) - 1  # Number of matrices
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    calculations = []

    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    def get_calculation_order(i, j):
        if i == j:
            return "A" + str(i + 1)
        else:
            k = split[i][j]
            left_calc = get_calculation_order(i, k)
            right_calc = get_calculation_order(k + 1, j)
            calculations.append((left_calc, right_calc, dimensions[i] * dimensions[k + 1] * dimensions[j + 1]))
            return f"({left_calc})({right_calc})"

    order = get_calculation_order(0, n - 1)
    calculations.reverse()  # Reverse the list to maintain order of calculations
    return dp[0][-1], order, calculations

# Example usage:
matrix_dimensions = [10, 30, 5, 50, 60]
min_operations, order, calc_list = matrix_chain_multiplication_order(matrix_dimensions)

print("Minimum number of multiplications:", min_operations)
print("Optimal order of multiplication:", order)

print("\nRequired sequence and calculations:")
for calc in calc_list:
    left_calc, right_calc, calc_cost = calc
    print(f"{left_calc} x {right_calc} = {calc_cost} operations")

# Additional calculations
total_operations = sum(calc[2] for calc in calc_list)
print("\nTotal operations (including considered):", total_operations)