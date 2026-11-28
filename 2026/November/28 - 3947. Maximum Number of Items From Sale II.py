class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)
        min_price = float('inf')
        max_factor = 0

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)
            max_factor = max(max_factor, factor)

        free = [0] * (max_factor + 1)

        for i in range(1, max_factor + 1):
            count = 0

            for j in range(i, max_factor + 1, i):
                count += freq[j]

            free[i] = count - 1

        offers = {}

        for factor, price in items:
            if price < 2 * min_price and free[factor] > 0:
                offers[price] = offers.get(price, 0) + free[factor]

        ans = 0

        for price in sorted(offers):
            count = min(offers[price], budget // price)

            ans += count * 2
            budget -= count * price

        ans += budget // min_price

        return ans
