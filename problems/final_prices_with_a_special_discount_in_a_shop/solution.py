class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(prices)):
            judge = False
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    judge = True
                    break
            
            if not judge:
                ans.append(prices[i])
                


        return ans

