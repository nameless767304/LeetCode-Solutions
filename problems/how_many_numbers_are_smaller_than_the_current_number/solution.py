class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_info = {}
        ans_info = {}
        
        for num in nums:
            nums_info[num] = nums_info.get(num, 0) + 1

        sorted_nums_info = dict(sorted(nums_info.items(), key = lambda x: x[0]))

        count_sum = 0
        for num, count in sorted_nums_info.items():
            ans_info[num] = count_sum
            count_sum += count

        return [ans_info[num] for num in nums]
