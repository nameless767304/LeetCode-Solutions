class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:

            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack: 
                    return False
                if c == ')':
                    if stack.pop() != '(':
                        return False
                elif c == ']': 
                    if stack.pop() != '[':
                        return False
                elif c =='}':
                    if stack.pop() != '{':
                        return False
                    
        if stack: return False
        else: return True
                
