class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s, idx_t = 0, 0
        
        while idx_s < len(s) and idx_t < len(t):
            if t[idx_t] == s[idx_s]:
                idx_t += 1
                idx_s += 1
            else:
                idx_t += 1

        if idx_s == len(s):
            return True
        else:
            return False