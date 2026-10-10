class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        nums_diff = {}
        k = k1 + k2
        ans = 0

        for i in range(len(nums1)):
            nums_diff[abs(nums1[i] - nums2[i])] = nums_diff.get(abs(nums1[i] - nums2[i]), 0) + 1

        nums = sorted(nums_diff.keys())

        while k and nums:
            num = nums.pop()
            if not num:
                break 

            count = nums_diff.pop(num)
            next_num = nums[-1] if nums else 0
            diff = num - next_num
            
            cost = count * diff

            if cost <= k:
                k -= cost
                nums_diff[next_num] = nums_diff.get(next_num, 0) + count
            else:
                q, r = divmod(k, count)
                nums_diff[num - q - 1] = nums_diff.get(num - q - 1, 0) + r
                nums_diff[num - q] = nums_diff.get(num - q, 0) + (count - r)
                k = 0
                break
    
        for num, count in nums_diff.items():
            ans += (num ** 2) * count

        return ans