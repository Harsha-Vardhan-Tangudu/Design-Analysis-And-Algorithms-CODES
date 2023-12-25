def backtracking_coin_change(denominations, amount):
    def backtrack(remaining, path):
        nonlocal result
        if remaining == 0:
            if not result or len(path) < len(result):
                result[:] = path[:]
            return
        for coin in denominations:
            if coin <= remaining:
                path.append(coin)
                backtrack(remaining - coin, path)
                path.pop()

    result = []
    backtrack(amount, [])
    return result if result else "Change not possible with the given denominations."

# Example usage:
denominations = [8, 5, 1]
amount = 30
backtracking_result = backtracking_coin_change(denominations, amount)
print("\nBacktracking Approach:")
print("Coins:", backtracking_result)