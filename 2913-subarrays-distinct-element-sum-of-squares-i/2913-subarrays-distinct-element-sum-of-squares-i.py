class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for idx1 in range(len(nums)):
            for idx2 in range(idx1, len(nums)):
                dv = len(set(nums[idx1:idx2 + 1]))
                ans += dv ** 2

        return ans