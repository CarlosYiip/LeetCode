class Solution(object):
    def numTrees(self, n):
        l = [0 for i in range(n+2)]
        l[0] = l[1] = 1
        
        for i in range(2, n+2):
            for j in range(1, i):
                l[i] += l[j] * l[i-j]
            
        return l[n+1]
