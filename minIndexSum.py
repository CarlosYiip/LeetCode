class Solution(object):
    def findRestaurant(self, list1, list2):
        d1 = dict()
        for i in range(len(list1)):
            d1[list1[i]] = i
        d2 = dict()
        m = float('inf')
        for i in range(len(list2)):
            if list2[i] in d1:
                score = d1[list2[i]] + i
                d2[list2[i]] = score
                m = min(score, m)
        res = []
        for name in d2:
            if d2[name] == m:
                res.append(name)
        return res
