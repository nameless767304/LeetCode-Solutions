class Solution:
    def rotatedDigits(self, n: int) -> int:
        comp_good_number = {'1','2','5','6','8','9','0'}
        count = 0

        for num in range(1, n + 1):
            num_set = set(str(num))
            if num_set.issubset(comp_good_number):
                num_set -= {'1','8','0'}
                if num_set:
                    count += 1

        return count
