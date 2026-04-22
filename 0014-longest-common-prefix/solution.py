class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort(key=len)

        for idx in range(len(strs[0])):
            for word in strs[1:]:
                if strs[0][idx] == word[idx]:
                    continue
                else:
                    return ans
                
            ans += strs[0][idx]

        return ans
