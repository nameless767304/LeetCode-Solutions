class Solution:
    def countCommas(self, n: int) -> int:
        count = 1
        criteria = 10 ** 3
        answer = 0

        while n >= criteria:
            answer += (n - criteria + 1)
            criteria *= 10 ** 3

        return answer
            
