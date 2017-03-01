class Solution(object):
    def inorder(self, node, l):
        if not node:
            return
        if node.left:
            self.inorder(node.left, l)
        l.append(node.val)
        if node.right:
            self.inorder(node.right, l)
    
    def getMinimumDifference(self, root):
        l = []
        self.inorder(root, l)
        min_diff = float('inf')
        for i in range(1, len(l)):
            this_diff = abs(l[i] - l[i-1])
            min_diff = min(this_diff, min_diff)
        return min_diff
