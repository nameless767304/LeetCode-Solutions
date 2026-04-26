class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_max = 0

        count = 0
        for num in nums:
            if num:
                count += 1
            else:
                count_max = max(count_max, count)
                count = 0


        return max(count_max, count)
