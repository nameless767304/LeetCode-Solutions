class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        length = len(nums)
        for idx in range(length // 2):
            ans.append(nums[idx])
            ans.append(nums[idx + length // 2])

        return ans


