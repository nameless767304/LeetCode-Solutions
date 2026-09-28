class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            ans = max(ans, depth)

        return ans
        