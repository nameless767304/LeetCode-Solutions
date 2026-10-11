class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        nums_length = len(nums)

        for idx, num in enumerate(nums):
            if nums_length % (idx + 1) == 0:
                ans += num ** 2

        return ans

