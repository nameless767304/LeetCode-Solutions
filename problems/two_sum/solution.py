class Solution(object):
    def twoSum(self, nums, target):
        for idx_num1 in range(len(nums)):
            for idx_num2 in range(idx_num1 + 1, len(nums)):
                if nums[idx_num1] + nums[idx_num2] == target:
                    return [idx_num1, idx_num2]

        