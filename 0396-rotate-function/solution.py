class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        length_nums = len(nums)
        F, ans = 0, 0

        for idx, num in enumerate(nums):
            F += idx * num
        ans = F

        for idx in range(length_nums - 1, 0, -1):
            F = F + sum_nums - length_nums * nums[idx]
            ans = max(F, ans)

        return ans


