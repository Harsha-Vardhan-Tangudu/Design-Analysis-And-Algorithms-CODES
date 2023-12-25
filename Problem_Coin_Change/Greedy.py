def greedy_coin_change(denominations, amount):
    denominations.sort(reverse=True)
    result = []
    total_coins = 0

    for coin in denominations:
        while amount >= coin:
            result.append(coin)
            amount -= coin
            total_coins += 1

    if amount == 0:
        return result, total_coins
    else:
        return "Change not possible with the given denominations."

# Example usage:
denominations = [8, 5, 1]
amount = 30
greedy_result, greedy_coins = greedy_coin_change(denominations, amount)
print("Greedy Approach:")
print("Coins:", greedy_result)
print("Total Coins:", greedy_coins)