# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.inorder = []
    
    def helper1(self, node):
        if not node:
            return
        self.helper1(node.left)
        self.inorder.append(node.val)
        self.helper1(node.right)
    
    def helper2(self, node):
        if not node:
            return
        self.helper2(node.left)
        node.val = self.inorder.pop(0)
        self.helper2(node.right)
    
    def convertBST(self, root):
        self.helper1(root)
        running_sum = 0
        for i in range(len(self.inorder) - 1, -1 ,-1):
            temp = self.inorder[i]
            self.inorder[i] += running_sum
            running_sum += temp
        self.helper2(root)
        return root
