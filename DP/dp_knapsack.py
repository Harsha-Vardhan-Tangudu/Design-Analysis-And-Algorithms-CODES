def knapsack_max_value(weights, values, knapsack_capacity, num_items, memoization_table):
    # Base conditions
    if num_items == 0 or knapsack_capacity == 0:
        return 0, []

    # Check if the result is already memoized
    if memoization_table[num_items][knapsack_capacity][0] != -1:
        return memoization_table[num_items][knapsack_capacity]

    # Choice diagram code
    if weights[num_items - 1] <= knapsack_capacity:
        # Include the current item in the knapsack
        included_value, included_items = knapsack_max_value(
            weights, values, knapsack_capacity - weights[num_items - 1], num_items - 1, memoization_table
        )
        included_value += values[num_items - 1]

        # Exclude the current item from the knapsack
        excluded_value, excluded_items = knapsack_max_value(
            weights, values, knapsack_capacity, num_items - 1, memoization_table
        )

        # Choose the maximum value between including and excluding the current item
        if included_value > excluded_value:
            chosen_items = included_items + [num_items - 1]
            memoization_table[num_items][knapsack_capacity] = included_value, chosen_items
        else:
            memoization_table[num_items][knapsack_capacity] = excluded_value, excluded_items

        return memoization_table[num_items][knapsack_capacity]

    # If the current item's weight exceeds the knapsack capacity, exclude it
    else:
        memoization_table[num_items][knapsack_capacity] = knapsack_max_value(
            weights, values, knapsack_capacity, num_items - 1, memoization_table
        )
        return memoization_table[num_items][knapsack_capacity]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
knapsack_capacity = 5
num_items = len(weights)

# Initialize the memoization table with -1
memoization_table = [[(-1, []) for _ in range(knapsack_capacity + 1)] for _ in range(num_items + 1)]

result_value, chosen_items = knapsack_max_value(weights, values, knapsack_capacity, num_items, memoization_table)
print("Maximum value:", result_value)
print("Chosen items:", chosen_items)