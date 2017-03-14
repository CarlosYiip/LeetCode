class Solution(object):
    def __init__(self):
        self.res = float('inf')
        
    def helper(self, node, target):
        if not node:
            return
        if abs(self.res-target) > abs(node.val-target):
            self.res = node.val
        if node.left and target < node.val:
            self.helper(node.left, target)
        if node.right and target > node.val:
            self.helper(node.right, target)
        return
        
    def closestValue(self, root, target):
        self.helper(root, target)
        return self.res
        
