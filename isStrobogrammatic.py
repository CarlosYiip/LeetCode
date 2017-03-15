class Solution(object):
    def isStrobogrammatic(self, num):
        s = {'0','1','6','8','9'}
        d = {'9':'6', '6':'9'}
        res = []
        
        for i in num[::-1]:
            if i not in s:
                return False
            if i == '9' or i == '6':
                res.append(d[i])
            else:
                res.append(i)
        return ''.join(res) == num
