class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curr = 0

        preSum = {0: 1}

        for num in nums:
            curr += num
            val = curr - k
            if val in preSum:
                ans += preSum[val]

            preSum[curr] = preSum.get(curr, 0) + 1

        return ans
