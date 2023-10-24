import math


def min_speed(piles, H):
    def can_eat_all(piles, K, H):
        hours_needed = 0
        for pile in piles:
            hours_needed += math.ceil(pile / K)
        return hours_needed <= H

    low = 1
    high = max(piles)

    while low <= high:
        mid = (low + high) // 2
        if can_eat_all(piles, mid, H):
            high = mid - 1
        else:
            low = mid + 1

    return low


print(min_speed([1000000000-30, 6, 7, 11], 1000000000))
print(min_speed([30, 11, 23, 4, 20], 5))
print(min_speed([30, 11, 23, 4, 20], 6))
print(min_speed([5, 8, 10, 12], 6))
