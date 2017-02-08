# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def helper(self, node, counter, current_max):
        if not node:
            return 0, current_max
        left_subsum, current_max = self.helper(node.left, counter, current_max)
        right_subsum, current_max = self.helper(node.right, counter, current_max)
        subsum = node.val + left_subsum + right_subsum
        if subsum not in counter:
            counter[subsum] = 1
        else:
            counter[subsum] += 1
        current_max = max(counter[subsum], current_max)
        return subsum, current_max
    
    def findFrequentTreeSum(self, root):
        if not root:
            return []
        counter = dict()
        current_max = 0
        a, current_max = self.helper(root, counter, current_max)
        return [k for k in counter if counter[k] == current_max]
