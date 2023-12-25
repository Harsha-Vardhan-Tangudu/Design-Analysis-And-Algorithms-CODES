# Iterative approach
def fibonacci_iterative(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


# Recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Dynamic Programming approach
def fibonacci_dynamic(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


# Driver code
n = int(input("Enter the number: "))
print("Fibonacci number using iterative approach: ", fibonacci_iterative(n))
print("Fibonacci number using recursive approach: ", fibonacci_recursive(n))
print("Fibonacci number using dynamic programming approach: ", fibonacci_dynamic(n))