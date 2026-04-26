class Solution:
    def minOperations(self, nums: list[int]) -> int:
        x = 0
        
        for idx in range(-1, - len(nums), -1):
            if nums[idx] < nums[idx - 1]:
                diff = nums[idx - 1] - nums[idx]
                x += diff

        return x
