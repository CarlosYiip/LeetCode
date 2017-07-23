class Solution(object):
    def helper(self, node):
        string = str(node.val)
        if node.left and node.right:
            left_string = "(" + self.helper(node.left) + ")"
            string += left_string
            right_string = "(" + self.helper(node.right) + ")"
            string += right_string
        elif node.left:
            left_string = "(" + self.helper(node.left) + ")"
            string += left_string
        elif node.right:
            right_string = "(" + self.helper(node.right) + ")"
            string += "()"
            string += right_string

        return string
        
    def tree2str(self, t):
        if not t:
            return ""
        return self.helper(t)
