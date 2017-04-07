class Solution(object):
    def helper(self, node):
        if not node.left:
            return node
        flipped = self.helper(node.left)
        target = flipped
        while target.right:
            target = target.right
        target.left, target.right = node.right, node
        node.left, node.right = None, None
        return flipped
    
    def upsideDownBinaryTree(self, root):
        if not root:
            return []
        return self.helper(root)
