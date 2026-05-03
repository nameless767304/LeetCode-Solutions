class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = []
        
        for idx1 in range(length - 1):
            count = 0
            for idx2 in range(idx1 + 1, length):
                if (nums[idx1] % 2 and not nums[idx2] % 2) or (not nums[idx1] % 2 and nums[idx2] % 2):
                    count += 1

            ans.append(count)
                
        ans.append(0)

        return ans
