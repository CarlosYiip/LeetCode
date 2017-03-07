class Solution(object):
    def helper(self, node, all_heights):
        if not node:
            return 0
        height = max(self.helper(node.left, all_heights), self.helper(node.right, all_heights)) + 1
        if height in all_heights:
            all_heights[height].append(node.val)
        else:
            all_heights[height] = [node.val]
        return height
    
    def findLeaves(self, root):
        all_heights = dict()
        self.helper(root, all_heights)
        res = [all_heights[k] for k in all_heights]
        return res
