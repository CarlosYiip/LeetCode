class Solution(object):
    def __init__(self):
        self.res = 0
        
    def calculate_height(self, node):
        if not node:
            return 0, 0
        left_subtree_height, a = self.calculate_height(node.left)
        right_subtree_height, b = self.calculate_height(node.right)
        height_of_this_node = max([left_subtree_height, right_subtree_height])
        self.res = max([self.res, left_subtree_height + right_subtree_height])
        return height_of_this_node + 1, left_subtree_height + right_subtree_height
        
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.calculate_height(root)
        return self.res
