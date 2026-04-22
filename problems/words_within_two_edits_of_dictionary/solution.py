class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []

        for word in queries:
            for word_dict in dictionary:
                count = 0
                
                for c1, c2 in zip(word, word_dict):
                    if c1 != c2:
                        count += 1
                    if count > 2:
                        break
                if count <= 2:
                    ans.append("".join(word))
                    break

        return ans

        