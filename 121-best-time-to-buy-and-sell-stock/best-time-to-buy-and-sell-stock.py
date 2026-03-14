class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        

        for p in prices[1:]:

            profit = p - min_price
            max_profit = max(max_profit, (p - min_price))
            if p < min_price:
                min_price = p
        
        return max_profit

