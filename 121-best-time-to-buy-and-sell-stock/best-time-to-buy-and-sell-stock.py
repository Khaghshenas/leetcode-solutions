class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        max_profit = 0

        left = 0
        for right in range(1, n):
            
            max_profit = max(max_profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
        
        return max_profit



