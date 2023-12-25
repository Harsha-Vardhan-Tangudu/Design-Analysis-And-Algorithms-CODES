def fractional_knapsack_backtrack(values, weights, capacity, current_value, current_weight, index, result):
    if index == len(values):
        result.append((current_value, current_weight))
        return

    if current_weight + weights[index] <= capacity:
        fractional_knapsack_backtrack(
            values, weights, capacity, current_value + values[index],
            current_weight + weights[index], index + 1, result
        )

    fractional_knapsack_backtrack(
        values, weights, capacity, current_value, current_weight, index + 1, result
    )

def fractional_knapsack(values, weights, capacity):
    result = []
    fractional_knapsack_backtrack(values, weights, capacity, 0, 0, 0, result)

    # Sort the results by value-to-weight ratio in descending order
    result.sort(key=lambda x: x[0] / x[1] if x[1] != 0 else float('inf'), reverse=True)

    return result

# Example driver code
values = [30, 40, 45, 77, 90]
weights = [5, 10, 15, 22, 25]  # Adding a zero-weight item
capacity = 60

result = fractional_knapsack(values, weights, capacity)

print("Items included in the knapsack:")
for value, weight in result:
    print(f"Value: {value}, Weight: {weight}")