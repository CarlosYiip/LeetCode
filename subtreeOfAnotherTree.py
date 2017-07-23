class Solution(object):
    def height(self, node):
        if not node:
            return 0
        cur_height = max(self.height(node.left) + 1, self.height(node.right) + 1)
        node.val = (node.val, cur_height)
        return cur_height
    
    def is_same_tree(self, n1, n2):
        if not n1 and not n2:
            return True
        if n1 and n2:
            if n1.val[0] == n2.val[0]:
                return self.is_same_tree(n1.left, n2.left) and self.is_same_tree(n1.right, n2.right)
            else:
                return False
        else:
            return False
 
    def helper(self, s, t):
        if not s:
            return False
        if s.val[1] == t.val[1]:
            return self.is_same_tree(s, t)
        else:
            return self.helper(s.left, t) or self.helper(s.right, t)
    
        
    def isSubtree(self, s, t):
        t_height = self.height(t)
        s_height = self.height(s)
        return self.helper(s, t)
