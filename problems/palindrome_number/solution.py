class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        nums = []
        while x:
            temp = x % 10
            nums.append(temp)
            x //= 10

        for idx in range(len(nums) // 2):
            if nums[idx] == nums[- idx - 1]:
                continue
            else:
                return False

        return True
