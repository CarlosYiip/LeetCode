class Solution(object):
    def reverseStr(self, s, k):
        res = []
        i = 0
        
        while i < len(s):
            if len(s) - i < k:
                for j in range(len(s)-1, i-1, -1):
                    res.append(s[j])
                break
            elif len(s) - i < 2*k:
                for j in range(i+k-1, i-1, -1):
                    res.append(s[j])
                for j in range(i+k, len(s)):
                    res.append(s[j])
                break
            else:
                for j in range(i+k-1, i-1, -1):
                    res.append(s[j])
                for j in range(i+k, i+2*k):
                    res.append(s[j])
                i += 2*k
        
        return ''.join(res)
