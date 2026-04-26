class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        judges = [False for _ in range(len(nums))]
        ans = []

        for num in nums:
            judges[num - 1] = True

        for idx, judge in enumerate(judges):
            if not judge:
                ans.append(idx + 1)

        return ans


