from collections import Counter
from heapq import *
class Solution(object):
    def frequencySort(self, s):
        c = Counter(s)
        l = [(c[key], key) for key in c]
        heapify(l)
        res = []
        while l:
            m = heappop(l)
            res.insert(0, m[1]*m[0])
        return ''.join(res)
