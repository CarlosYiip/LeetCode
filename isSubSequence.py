class Solution(object):
    def isSubsequence(self, s, t):
        # i,j = 0,0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == len(s)
        t = iter(t)
        return all(c in t for c in s)
