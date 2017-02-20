# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, node, nums):
        if not node:
            return
        if node.left:
            self.inorder(node.left, nums)
        node.val = nums.pop(0)
        if node.right:
            self.inorder(node.right, nums)
    
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        if len(nums) == 2:
            root = TreeNode(nums[0])
            root.right = TreeNode(nums[1])
            return root
            
        l = [TreeNode(None) for i in range(len(nums) + 1)]
        
        for i in range(1, len(l)):
            if 2 * i < len(l):
                l[i].left = l[2 * i]
            if 2 * i + 1 < len(l):
                l[i].right = l[2 * i + 1]
        
        root = l[1]
        self.inorder(root, nums)
        
        return root
