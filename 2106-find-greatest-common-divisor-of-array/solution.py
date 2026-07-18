class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest_number = min(nums)
        largest_number = max(nums)
        ans = smallest_number

        while True:
            if not largest_number % ans and not smallest_number % ans:
                return ans
            else:
                ans -= 1
