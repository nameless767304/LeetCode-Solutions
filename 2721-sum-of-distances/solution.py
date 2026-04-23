class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        length = len(nums)
        arr = [0 for _ in range(length)]
        nums_idx = dict((num, []) for num in set(nums))
        nums_sum = dict((num, [0, 0]) for num in set(nums))
        nums_count = dict((num, [0, 0]) for num in set(nums))

        for idx in range(length):
            nums_idx[nums[idx]].append(idx)
            nums_count[nums[idx]][1] += 1

        for num, idxs in nums_idx.items():
            nums_sum[num][1] = sum(idxs)

        for idx in range(len(nums)):
            if nums_count[nums[idx]][0] == 0 and nums_count[nums[idx]][1] == 1:
                arr[idx] = 0
                continue

            left = nums_count[nums[idx]][0] * idx - nums_sum[nums[idx]][0]
            right = nums_sum[nums[idx]][1] - (nums_count[nums[idx]][1] - 1) * idx - idx
            arr[idx] = left + right

            nums_sum[nums[idx]][0] += idx
            nums_sum[nums[idx]][1] -= idx
            nums_count[nums[idx]][0] += 1
            nums_count[nums[idx]][1] -= 1

        return arr

