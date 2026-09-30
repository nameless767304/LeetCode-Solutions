class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0

        for c in seq:
            if c == "(":
                depth += 1
                ans.append(depth % 2)
            elif c == ")":
                ans.append(depth % 2)
                depth -= 1
                
        return ans

