class Solution:
    def checkString(self, s: str) -> bool:
        status = False
        
        for c in s:
            if c == 'b' and status == False:
                status = True
            elif c == 'a' and status == True:
                return False
            
        return True