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

#Optimal Approach

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        result = 0
        mod = 10**9 + 7
        
        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1] + arr[i]

        even = 1
        odd = 0
        for i in range(n):
            if prefix[i] % 2 == 0:
                result = (result + odd) % mod
                even += 1
            else:
                result = (result + even) % mod
                odd += 1

        return result
