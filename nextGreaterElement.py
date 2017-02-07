class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        d = dict()
        stack = list()
        
        for i in nums:
            while stack:
                if stack[-1] < i:
                    d[stack.pop()] = i
                else:
                    break
            stack.append(i)
            
        res = []
        for i in findNums:
            res.append(d.setdefault(i, -1))
            
        return res
