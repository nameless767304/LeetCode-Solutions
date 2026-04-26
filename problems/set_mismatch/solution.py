class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup_num = -1
        check = [False for _ in range(len(nums))]

        for num in nums:
            if check[num -1]:
                dup_num = num
            else:
                check[num - 1] = True
            
        for idx in range(len(check)):
            if not check[idx]:
                return [dup_num, idx + 1]
            