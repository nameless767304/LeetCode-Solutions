class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for idx1 in range(len(nums)):
            s = set()
            for idx2 in range(idx1, len(nums)):
                s.add(nums[idx2])
                ans += len(s) ** 2
                
        return ans