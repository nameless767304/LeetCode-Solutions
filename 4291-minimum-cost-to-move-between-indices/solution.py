class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        length = len(nums)
        preSum_left = [0] * length
        preSum_right = [0] * length
        ans = []

        for idx in range(length - 1, 0, -1):
            cost = 1
            if idx < length - 1:
                dist_L = nums[idx] - nums[idx - 1]
                dist_R = nums[idx + 1] - nums[idx]
                if dist_L > dist_R:
                    cost = dist_L
            preSum_left[idx - 1] = preSum_left[idx] + cost

        for idx in range(length - 1):
            cost = 1
            if idx > 0:
                dist_L = nums[idx] - nums[idx - 1]
                dist_R = nums[idx + 1] - nums[idx]
                if dist_L <= dist_R:
                    cost = dist_R
            preSum_right[idx + 1] = preSum_right[idx] + cost

        for idx1, idx2 in queries:
            if idx1 < idx2:
                ans.append(preSum_right[idx2] - preSum_right[idx1])
            elif idx1 > idx2:
                ans.append(preSum_left[idx2] - preSum_left[idx1])
            else:
                ans.append(0)

        return ans
