class Solution(object):
    def generatePossibleNextMoves(self, s):
        s = [i for i in s]
        if len(s) < 2:
            return []
        res = []
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i+1] == '+':
                l = [c for c in s]
                l[i], l[i+1] = '-', '-'
                res.append(''.join(l))
        return res
