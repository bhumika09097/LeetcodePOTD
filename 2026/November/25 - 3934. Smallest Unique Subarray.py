# Brute Force Appoach (TLE)
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        for windowSize in range(1, n + 1):
            subarrays = []

            for i in range(n - windowSize + 1):
                subarrays.append(tuple(nums[i:i + windowSize]))

            freq = {}

            for sub in subarrays:
                freq[sub] = freq.get(sub, 0) + 1

            for count in freq.values():
                if count == 1:
                    return windowSize

        return n


# Optimal Approach
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # Binary exponentiation
        def pow(a, power):
            if power == 0:
                return 1

            half = pow(a, power // 2)
            result = (half * half) % MOD

            if power % 2 == 1:
                result = (result * a) % MOD

            return result

        # Sliding Window + Rolling Hash
        def check(size, base):
            h = 0
            mp = {}

            p = pow(base, size - 1)

            i = j = 0

            while j < n:
                h = (h * base + nums[j]) % MOD

                if j - i + 1 < size:
                    j += 1
                else:
                    mp[h] = mp.get(h, 0) + 1

                    h = (h - (p * nums[i]) % MOD + MOD) % MOD

                    i += 1
                    j += 1

            return any(count == 1 for count in mp.values())

        # Binary Search
        base = max(nums) + 1

        left, right = 1, n
        result = n

        while left <= right:
            mid = (left + right) // 2

            if check(mid, base):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
