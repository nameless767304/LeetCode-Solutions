class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            else:
                if not stack:
                    return False
                if c != stack.pop():
                    return False
        
        return False if stack else True