class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 2: return nums
    
        is_valid = [False] * n
        is_valid[0] = is_valid[n-1] = True
        
        left_max = nums[0]
        for i in range(1, n - 1):
            if nums[i] > left_max:
                is_valid[i] = True
                left_max = nums[i]
                
        right_max = nums[n-1]
        for i in range(n - 2, 0, -1):
            if nums[i] > right_max:
                is_valid[i] = True
                right_max = nums[i]

        return [nums[i] for i in range(n) if is_valid[i]]
