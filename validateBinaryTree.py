# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, node, l):
        if not node:
            return
        if node.left:
            self.inorder(node.left, l)
        l.append(node.val)
        if node.right:
            self.inorder(node.right, l)
    
    
    
    def isValidBST(self, root):
        l = []
        self.inorder(root, l)
        for i in range(len(l)-1):
            if l[i+1] <= l[i]:
                return False
        return True
