class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ans = []
        
        for i in range(k, 0, -1):
            ans.append(s[i - 1])

        for i in range(k, len(s)):
            ans.append(s[i])

        return "".join(ans)
