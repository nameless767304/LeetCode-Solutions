class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(map(str, digits))
        num = int(num) + 1
        num = list(str(num))
        
        for idx in range(len(num)):
            num[idx] = int(num[idx])
        
        return num
