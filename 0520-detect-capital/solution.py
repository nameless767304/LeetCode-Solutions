class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        upperword = word.upper()
        lowerword = word.lower()

        if word == upperword or word == lowerword or (word[0] == upperword[0] and word[1:] == lowerword[1:]):
            return True
        
        return False
