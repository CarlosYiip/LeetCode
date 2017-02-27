class Solution(object):
    def flip(self, comb, N):
        d = dict()
        for i in comb:
            d[i] = 1
        return [i for i in range(1, N+1) if i not in d]
    
    
    def helper(self, temp, start, end, k, res, flipped):
        if len(temp) == k:        
            if not flipped:
                res.append([i for i in temp])
            else:
                res.append(self.flip(temp, end))
            return
    
        for i in range(start, end+1):
            temp.append(i)
            start = temp[-1] + 1
            self.helper(temp, start, end, k, res, flipped)
            temp.pop()

    def combine(self, n, k):
        flipped = False
        if k > n - k:
            flipped = True
            k = n - k
        res = []
        self.helper([], 1, n, k, res, flipped)
        return res
