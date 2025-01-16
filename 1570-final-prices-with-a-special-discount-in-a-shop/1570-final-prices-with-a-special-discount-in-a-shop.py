class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        stack = []
        n = n - 1
        while n >= 0:
            while stack and stack[-1] > prices[n]:
                stack.pop()
            
            if not stack:
                ans[n] = prices[n]
                stack.append(prices[n])
            else:
                ans[n] = prices[n] - stack[-1]
                stack.append(prices[n])
            n -= 1
        
        return ans
        