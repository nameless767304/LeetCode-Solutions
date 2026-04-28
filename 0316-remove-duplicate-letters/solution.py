class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        used = set()

        for idx, c in enumerate(s):
            if not stack:
                stack.append(idx)
                used.add(c)
                continue 

            if c == s[stack[-1]]:
                continue
            elif c > s[stack[-1]]:
                if c in used:
                    continue
                else:
                    stack.append(idx)
                    used.add(c)
            
            else:
                while stack and s[stack[-1]] in s[idx:] and s[stack[-1]] > c:
                    if c in used:
                        break
                    else:
                        used.remove(s[stack.pop()])

                if c in used:
                    continue
                else:
                    stack.append(idx)
                    used.add(c)

        
        return "".join([s[idx] for idx in stack])
