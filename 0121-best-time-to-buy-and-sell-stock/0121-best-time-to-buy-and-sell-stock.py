class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            profit = max(0, profit + (prices[i] - prices[i-1]))
            maxProfit = max(maxProfit, profit)
        return maxProfit

        
                
            