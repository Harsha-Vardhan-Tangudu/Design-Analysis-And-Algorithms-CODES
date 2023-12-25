import heapq

def branch_and_bound_coin_change(denominations, amount):
    denominations.sort(reverse=True)
    heap = [(0, 0, [])]  # (total coins, remaining amount, current path)
    result = []

    while heap:
        total_coins, remaining, path = heapq.heappop(heap)

        if remaining == 0:
            result = path[:]
            break

        for coin in denominations:
            if coin <= remaining:
                heapq.heappush(heap, (total_coins + 1, remaining - coin, path + [coin]))

    return result if result else "Change not possible with the given denominations."

# Example usage:
denominations = [8, 5, 1]
amount = 30
bb_result = branch_and_bound_coin_change(denominations, amount)
print("\nBranch and Bound Approach:")
print("Coins:", bb_result)