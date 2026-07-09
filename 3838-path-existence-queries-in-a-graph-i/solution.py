class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], max_Diff: int, queries: List[List[int]]) -> List[bool]:
        preSum_diff = [1]
        answer = []
        for idx in range(1, n):
            temp = nums[idx] - nums[idx - 1]
            if temp <= max_Diff:
                preSum_diff.append(preSum_diff[-1] + 1)
            else:
                preSum_diff.append(preSum_diff[-1])
        
        for u, v in queries:
            u, v = min(u, v), max(u, v)
            if preSum_diff[v] - preSum_diff[u] == v - u:
                answer.append(True)
            else:
                answer.append(False)

        return answer


