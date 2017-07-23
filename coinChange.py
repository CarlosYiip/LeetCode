class Solution(object):
    def coinChange(self, coins, amount):
        dp = [-1 * (amount + 1)]
        dp[0] = 0
        for i in range(1, amount+1):
            a = float('inf')
            for j in coins:
                if i - j >= 0:
                    a = min(a, dp[i-j] + 1)
            dp.append(a)
    
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
        
