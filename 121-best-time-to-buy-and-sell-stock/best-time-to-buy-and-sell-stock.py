class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        current_max_profit = 0
        

        for right in range(1, len(prices)):

            if (prices[right] - prices[left]) > current_max_profit:
                current_max_profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
        
        return current_max_profit

