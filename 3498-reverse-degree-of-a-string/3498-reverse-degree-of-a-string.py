class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
        ans = 0

        for idx, c in enumerate(s):
            alphabet[c] = alphabet[c] + (idx + 1)
            
        for idx, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
            ans += alphabet[c] * (26 - idx)

        return ans
            
            

