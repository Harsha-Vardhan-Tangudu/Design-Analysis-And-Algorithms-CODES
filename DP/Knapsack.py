import random
import numpy as np

# Function to generate random values for weight and value
def generate_random_values(n):
    weight = []
    value = []
    for i in range(n):
        weight.append(random.randint(1, 100))
        value.append(random.randint(1, 100))
    return weight, value

# Function to implement knapsack problem using dynamic programming
def knapsack_dynamic_programming(weight, value, capacity, n):
    matrix = np.zeros((n+1, capacity+1), dtype=int)
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weight[i-1] <= j:
                matrix[i][j] = max(value[i-1] + matrix[i-1][j-weight[i-1]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[n][capacity]

if __name__ == "__main__":
    n = 10
    capacity = 50
    weight, value = generate_random_values(n)
    print("The weights of the items are: ", weight)
    print("The values of the items are: ", value)
    print("The maximum value of the knapsack is: ", knapsack_dynamic_programming(weight, value, capacity, n))