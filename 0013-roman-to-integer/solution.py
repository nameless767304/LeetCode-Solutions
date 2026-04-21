class Solution(object):
    def romanToInt(self, s):
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for idx in range(len(s) - 1):
            Roman_front = Roman[s[idx]]
            Roman_back = Roman[s[idx + 1]]
            if Roman_front >= Roman_back:
                res += Roman_front
            else:
                res -= Roman_front 

        res += Roman[s[-1]]

        return res

