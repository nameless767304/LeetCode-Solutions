class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            if not stack:
                stack.append(idx)
                continue

            while stack:
                if temperatures[stack[-1]] < temp:
                    idx_rec = stack.pop()
                    ans[idx_rec] = idx - idx_rec
                else:
                    break

            stack.append(idx)

        return ans
