# Recursion + Memoization

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        memo = [[-1] * 2 for _ in range(n)]
        def findMethod(start,target):
            l = start
            r = len(nums)-1
            ans = -1
            while l <= r:
                mid = (r+l) // 2

                if nums[mid] == target:
                    ans = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return ans

        def solve(i,inc):
            if memo[i][inc] != -1:
                return memo[i][inc]

            currval = nums[i] + inc
            length = 1

            j = findMethod(i+1,currval+1)
            if j != -1:
                length = max(length, 1 + solve(j,0))
            
            j = findMethod(i+1,currval)
            if j != -1:
                length = max(length, 1 + solve(j,1))

            memo[i][inc] = length
            return memo[i][inc]


        result = 1
        for i in range(n):
            result = max(
                result,
                solve(i,0),
                solve(i,1)
            )

        return result


