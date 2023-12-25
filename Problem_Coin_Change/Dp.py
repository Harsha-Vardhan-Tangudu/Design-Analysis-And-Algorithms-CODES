def dynamic_coin_change(denominations, amount):
    dp_table = [float('inf')] * (amount + 1)
    dp_table[0] = 0

    for coin in denominations:
        for i in range(coin, amount + 1):
            dp_table[i] = min(dp_table[i], dp_table[i - coin] + 1)

    if dp_table[amount] == float('inf'):
        return "Change not possible with the given denominations."
    else:
        coins = []
        i = amount
        while i > 0:
            for coin in denominations:
                if i - coin >= 0 and dp_table[i] == dp_table[i - coin] + 1:
                    coins.append(coin)
                    i -= coin
                    break

        return coins, dp_table[amount]

# Example usage:
denominations = [8, 5, 1]
amount = 30
dynamic_result, dynamic_coins = dynamic_coin_change(denominations, amount)
print("\nDynamic Programming Approach (Corrected):")
print("Coins:", dynamic_result)
print("Total Coins:", dynamic_coins)