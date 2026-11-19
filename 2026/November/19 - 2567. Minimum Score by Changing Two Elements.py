class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = min(abs(nums[2] - nums[-1]) , abs(nums[0] - nums[-3]) , abs(nums[1] - nums[-2]))
        return ans
