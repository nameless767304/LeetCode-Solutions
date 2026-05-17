class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        val = 0
        substring = word
        
        for _ in range(len(sequence) // len(substring)):
            if substring not in sequence:
                break
            else:
                val += 1
                substring += word

        return val
