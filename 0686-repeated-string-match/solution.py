class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        rep = b.count(a)
        s = a * rep

        if b in s:
            return rep
        elif b in s + a:
            return rep + 1
        elif b in s + a + a:
            return rep + 2
        else:
            return -1
