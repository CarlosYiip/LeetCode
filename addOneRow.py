class Solution(object):
    def addOneRow(self, node, v, d):
        if d - 1 == 1:
            if node.left:
                prev_left = node.left
                node.left = TreeNode(v)
                node.left.left = prev_left
            else:
                node.left = TreeNode(v)
            if node.right:
                prev_right = node.right
                node.right = TreeNode(v)
                node.right.right = prev_right
            else:
                node.right = TreeNode(v)
        elif d - 1 == 0:
            new_root = TreeNode(v)
            new_root.left = node
            return new_root
        else:
            if node.left:
                self.addOneRow(node.left, v, d - 1)
            if node.right:
                self.addOneRow(node.right, v, d - 1)
        return node
