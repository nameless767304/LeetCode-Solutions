class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_nums = []
        for num in nums:
            if not self.prefix_nums:
                self.prefix_nums.append(num)
                continue
                
            self.prefix_nums.append(num + self.prefix_nums[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_nums[right] - (self.prefix_nums[left - 1] if left != 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
