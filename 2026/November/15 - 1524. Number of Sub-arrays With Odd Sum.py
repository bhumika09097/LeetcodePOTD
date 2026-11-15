# Brtue Force Approch (TLE)
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        result = 0
        mod = 10**9 + 7
        for i in range(n):
            subarraysum = 0
            for j in range(i,n):
                subarraysum += arr[j]
                if subarraysum % 2 != 0:
                    result += 1

        return result % mod

  
