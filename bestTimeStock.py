class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
            
        max_profit, min_so_far, max_so_far = 0, prices[0], prices[0]
        for i in prices[1:]:
            if i < min_so_far:
                max_so_far, min_so_far = i, i
            elif i > max_so_far:
                max_so_far = i
            max_profit = max(max_profit, max_so_far - min_so_far)
        
        return max_profit
