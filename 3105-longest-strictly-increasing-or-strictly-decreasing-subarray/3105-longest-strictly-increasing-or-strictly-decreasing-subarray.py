class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        idx = 0
        desc_temp = 1
        insc_temp = 1
        
        while idx < (len(nums) - 1):
            if nums[idx] < nums[idx + 1]:
                desc_temp = 1
                insc_temp += 1
            elif nums[idx] > nums[idx + 1]:
                insc_temp = 1
                desc_temp += 1
            else:
                desc_temp = 1
                insc_temp = 1
            
            idx += 1
            ans = max(ans, desc_temp, insc_temp)
            
        return ans