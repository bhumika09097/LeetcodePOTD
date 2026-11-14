#Brute Force approach
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        result = float('inf')

        for i in range(n):
            for j in range(i,n):
                subarraysum = 0
                subarraylen = len(nums[i:j+1])
                if l <= subarraylen <= r:
                    for k in range(i,j+1):
                        subarraysum += nums[k]
                    if subarraysum > 0:
                        result = min(result , subarraysum)

        if result != float('inf'):
            return result
        return -1

  #optimal approach
  class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        result = float('inf')

        for i in range(n):
            for j in range(i, n):
                subarraylen = j - i + 1

                if l <= subarraylen <= r:
                    subarraysum = prefix[j + 1] - prefix[i]

                    if subarraysum > 0:
                        result = min(result, subarraysum)

        if result == float('inf'):
            return -1

        return result

