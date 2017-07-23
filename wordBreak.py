class Solution(object):
    def wordBreak(self, word, word_dict):
        word_dict = set(word_dict)
        dp = [False for i in range(len(word) + 1)]
        dp[0] = True
        for i in range(1, len(word)+1):
            if word[:i] in word_dict:
                dp[i] = True
            else:
                for j in range(i-1, -1, -1):
                    if word[j:i] in word_dict and dp[j]:
                        dp[i] = True
                        break
        return dp[-1]
