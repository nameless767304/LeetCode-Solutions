class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for idx in range(0, len(s), 2):
            if s[idx] == s[idx + 1]:
                continue
            else:
                ans += 1

        return ans