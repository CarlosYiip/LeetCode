class Solution(object):
    def nthUglyNumber(self, n):
        if (n <= 0):
            return 0
        elif n == 1:
            return 1
        t2, t3, t5 = 0, 0, 0
        dp = [0 for i in range(n)]
        dp[0] = 1
        
        for i in range(1, n):
            dp[i] = min(dp[t2]*2, dp[t3]*3, dp[t5]*5)
            if (dp[i] == dp[t2]*2):
                t2 += 1
            if (dp[i] == dp[t3]*3):
                t3 += 1
            if (dp[i] == dp[t5]*5):
                t5 += 1
        return dp[-1]
