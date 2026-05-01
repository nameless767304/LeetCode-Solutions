class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        if set(s) == {"-"}:
            return ""

        s = s.upper()
        filtered_s = []
        ans = []

        for c in s:
            if c != "-":
                filtered_s.append(c)            

        count = k - len(filtered_s) % k    
        for c in filtered_s:
            if count == k:
                ans.append('-')
                ans.append(c)
                count = 1
            else:
                ans.append(c)
                count += 1

        if ans[0] == "-":   ans = ans[1:]
        return "".join(ans)
                
