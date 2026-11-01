# Brute Force Approach 
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        moves = 0
        
        def allElementEqual(nums):
            for i in range(n):
                if nums[i] != nums[0]:
                    return False    
            return True

        while not allElementEqual(nums):
            maxElementIdx = nums.index(max(nums))
            for i in range(n):
                if i != maxElementIdx:
                    nums[i] += 1
                
            moves += 1

        return moves
# Optimal 
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        sum = 0
        minElement = min(nums)
        for i in range(n):
            sum += nums[i]

        return sum - (n*minElement)
        
