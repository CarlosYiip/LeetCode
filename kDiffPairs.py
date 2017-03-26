class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        res = 0
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        if k == 0:
            for i in d:
                if d[i] > 1:
                    res += 1
            return res
        else:
            for i in d:
                if i + k in d:
                    res += 1
            return res
