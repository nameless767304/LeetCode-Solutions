class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s = [int(n) for n in s]
        ans = ""

        while len(s) > k:
            print(s)
            temp = []
            for idx in range(0, len(s), k):
                group_sum = sum(s[idx:idx + k])
                temp.extend([int(digit) for digit in str(group_sum)])

            s = temp

        for n in s:
            ans += str(n)

        return ans