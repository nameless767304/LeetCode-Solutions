class Solution:
    def check(self, nums: List[int]) -> bool:
        is_pointed = False
        for idx in range(len(nums) - 1):
            if nums[idx] <= nums[idx + 1]:
                continue
            else:
                if is_pointed:
                    return False
                else:
                    is_pointed = True
                    continue

        if (is_pointed and nums[0] >= nums[-1]) or not is_pointed:
            return True
        else:
            return False

