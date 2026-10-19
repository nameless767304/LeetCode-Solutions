class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums.sort()
        for idx, num in enumerate(nums):
            if num == target:
                ans.append(idx)
            elif num > target: break

        return ans