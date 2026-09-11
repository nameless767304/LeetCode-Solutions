class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digits_length = len(digits)
        ans = set()
        
        for idx1 in range(digits_length):
            if digits[idx1] == 0:
                continue
                
            for idx2 in range(digits_length):
                for idx3 in range(digits_length):
                    if (idx1 == idx2 or idx2 == idx3 or idx1 == idx3) or digits[idx3] % 2: 
                        continue
                    ans.add(int(str(digits[idx1]) + str(digits[idx2]) + str(digits[idx3])))

        return len(ans)