class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[-1] * n for _ in range(n)]

        def getCost(start, end):
            if cost[start][end] != -1:
                return cost[start][end]

            length = end - start + 1
            answer = INF

            # Try all proper divisors
            for d in range(1, length):
                if length % d != 0:
                    continue

                changes = 0

                for offset in range(d):
                    left = start + offset
                    right = end - d + 1 + offset

                    while left < right:
                        if s[left] != s[right]:
                            changes += 1

                        left += d
                        right -= d

                answer = min(answer, changes)

            cost[start][end] = answer
            return answer

        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        def solve(start, parts_left):

            if parts_left == 0:
                return 0 if start == n else INF

            if n - start < 2 * parts_left:
                return INF

            if dp[start][parts_left] != -1:
                return dp[start][parts_left]

            answer = INF

            last_end = n - 2 * (parts_left - 1) - 1

            for end in range(start + 1, last_end + 1):

                current_cost = getCost(start, end)

                remaining_cost = solve(end + 1, parts_left - 1)

                answer = min(
                    answer,
                    current_cost + remaining_cost
                )

            dp[start][parts_left] = answer
            return answer

        return solve(0, k)
