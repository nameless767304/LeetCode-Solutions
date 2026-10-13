class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            nums[idx] = num ** 2

        nums.sort()

        return - sum(nums[:len(nums) // 2]) + sum(nums[len(nums) // 2:])