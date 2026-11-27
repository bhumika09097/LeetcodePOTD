class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        copies = [0] * n

        for i in range(n):
            for j in range(n):
                if items[j][0] % items[i][0] == 0:
                    copies[i] += 1

        cheapest = items[0][1]

        for i in range(1, n):
            if items[i][1] < cheapest:
                cheapest = items[i][1]
        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            value = copies[i]

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + value)

        ans = 0

        for i in range(budget + 1):
            extra = (budget - i) // cheapest

            total = dp[i] + extra

            if total > ans:
                ans = total

        return ans
