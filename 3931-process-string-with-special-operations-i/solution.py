class Solution:
    def processStr(self, s: str) -> str:
        ans = []

        for c in s:
            if c == '*':
                if ans: ans.pop()
            elif c == '#':
                ans.extend(ans)
            elif c == '%':
                ans.reverse()
            else:
                ans.append(c)

        return "".join(ans)
