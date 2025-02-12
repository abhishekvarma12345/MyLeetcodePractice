class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            profit += (prices[i] - prices[i-1]) 
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                profit = 0
        return maxProfit

        
                
            