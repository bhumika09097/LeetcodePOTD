# Withot build in function 
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        def gcd(a,b):
            while b:
                a , b = b , a % b 
            return a

        def lcm(a,b):
            if a == 0 or b == 0:
                return 0
            return abs(a*b) // gcd(a,b)

        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i,n):
                prod *= nums[j]
                g = gcd(g,nums[j])
                l = lcm(l,nums[j])

                if prod == g * l:
                    length = j - i + 1
                    result = max(result,length)

        return result


# Wtih Built in functions
import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i,n):
                prod *= nums[j]
                g = math.gcd(g,nums[j])
                l = math.lcm(l,nums[j])

                if prod == g * l:
                    length = j - i + 1
                    result = max(result,length)

        return result
