class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        primes = set()
        temp_num = int(str(n)[::-1])

        num1 = min(n, temp_num)
        num2 = max(n, temp_num)
        
        for num in range(max(2, num1), num2 + 1):
            judge = True
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    judge = False
                    break                    
            if judge:   primes.add(num)

        
        return sum(primes)

