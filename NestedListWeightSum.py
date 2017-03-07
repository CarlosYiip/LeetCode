class Solution(object):
    def helper(self, nestedList, depth):
        count = 0
        for i in nestedList:
            if i.isInteger():
                count += i.getInteger() * depth
            else:
                count += self.helper(i.getList(), depth + 1)
        return count
        
    def depthSum(self, nestedList):
        return self.helper(nestedList, 1)
        
