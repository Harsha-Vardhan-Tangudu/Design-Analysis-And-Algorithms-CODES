def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if capacity >= item[0]:
            # Take the whole item if there is enough capacity
            knapsack.append((item[0], item[1]))
            total_value += item[1]
            capacity -= item[0]
        else:
            # Take a fraction of the item if there is limited capacity
            fraction = capacity / item[0]
            knapsack.append((capacity, fraction * item[1]))
            total_value += fraction * item[1]
            break  # Stop adding items as the knapsack is full

    return total_value, knapsack

# Example usage
items = [(10, 60), (20, 100), (30, 120)]  # Format: (weight, value)
knapsack_capacity = 50

total_value, selected_items = fractional_knapsack(items, knapsack_capacity)

print("Selected items in the knapsack:")
for item in selected_items:
    print(f"Weight: {item[0]}, Value: {item[1]}")

print("Total Value:", total_value)