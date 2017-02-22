# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNode(self, node):
        if not node:
            return 0
        left_subtree_count = self.countNode(node.left)
        right_subtree_count = self.countNode(node.right)
        node.leftCount = left_subtree_count
        return 1 + left_subtree_count + right_subtree_count
        
    def kthSmallest(self, root, k):
        self.countNode(root)
        node = root
        while node:
            print(node.val, node.leftCount)
            if node.leftCount + 1 == k:
                return node.val
            if k <= node.leftCount:
                node = node.left
            else:
                k -= (node.leftCount + 1)
                node = node.right
