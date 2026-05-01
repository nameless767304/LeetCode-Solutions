class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        if len(s) == 1:
            return False

        for s_length in range(1, length // 2 + 1):
            s_set = set()
            if length % s_length == 0:
                for idx in range(0, len(s), s_length):
                    s_set.add(s[idx:idx + s_length])
                    if len(s_set) > 1:
                        break

                if len(s_set) == 1:
                    return True
        
        return False
                


