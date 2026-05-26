class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = set()
        uppercase = set()

        for c in word:
            C = c.upper()
            if c == C:
                uppercase.add(c.lower())
            else:
                lowercase.add(c)

        return len(lowercase.intersection(uppercase))

        
                
        
