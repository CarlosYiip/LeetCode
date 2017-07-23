class Solution(object):
    def minimumTotal(self, triangle):
        dp = triangle[0]
        
        for i in range(1, len(triangle)):
            tmp = dp
            dp = triangle[i]
            
            for j in range(len(dp)):
                if j == 0:
                    dp[0] += tmp[0]
                elif j == len(dp) - 1:
                    dp[-1] += tmp[-1]
                else:
                    dp[j] += min(tmp[j-1:j+1])
        return min(dp)