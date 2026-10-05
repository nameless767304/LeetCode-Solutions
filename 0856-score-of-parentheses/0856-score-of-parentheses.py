class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for idx, c in enumerate(s):
            if c == '(':
                stack.append(c)
            elif c == ')':
                if s[idx - 1] == '(':
                    stack.pop()
                    if stack and stack[-1] != '(':
                        stack.append(1 + stack.pop())
                    else:
                        stack.append(1)
                else:
                    temp = stack.pop() * 2
                    stack.pop()
                    stack.append(temp)

            if len(stack) > 2 and type(stack[-1]) == int and type(stack[-2]) == int:
                stack.append(stack.pop() + stack.pop())

        return sum(stack)