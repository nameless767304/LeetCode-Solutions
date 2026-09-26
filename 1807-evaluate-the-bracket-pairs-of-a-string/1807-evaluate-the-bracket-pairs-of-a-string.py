class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = ""
        judge = 0
        knowledge_dict = {k: v for k, v in knowledge}

        for c in s:
            if c == "(":
                temp = ""
                judge = 1
            elif c == ")":
                ans += knowledge_dict.get(temp, '?')
                judge = 0
            elif judge:
                temp += c
            else:
                ans += c

        return ans