class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        

        for p in range(1, len(prices)):

            if (prices[p] - min_price) > max_profit:
                max_profit = prices[p] - min_price
            if prices[p] < min_price:
                min_price = prices[p]
        
        return max_profit

