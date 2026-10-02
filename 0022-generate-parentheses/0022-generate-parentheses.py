class Solution:
    def __init__(self):
        self.ans = []
        self.n = None

    def generateParenthesis(self, n: int) -> list[str]:
        self.n = n
        self.recursionParenthesis("", 0, 0)

        return self.ans

    def recursionParenthesis(self, s, count_op, count_cl):
        if count_op < count_cl:
            return 

        if count_op + count_cl == 2 * self.n:   # Finish
            self.ans.append(s)
        else:   # 
            if count_op < self.n:
                self.recursionParenthesis(s + '(', count_op + 1, count_cl)
            if s:
                self.recursionParenthesis(s + ')', count_op, count_cl + 1)

        return 