class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if 0 < int(s[i-1] + s[i]) <= 26:
                    dp.append(dp[i-1])
                else:
                    return 0
            else:
                if 0 < int(s[i-1] + s[i]) <= 26 and s[i-1] != '0':
                    dp.append(dp[i-1] + dp[i])
                else:
                    dp.append(dp[i])
        return dp[-1]