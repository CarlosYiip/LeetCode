class Solution(object):
    def helper(self, res, nums, used, final):
        if len(res) == len(nums):
            final.append(res)
            return
        
        for i in nums:
            if i not in used or used[i] == 0:
                used[i] = 1
                n = [j for j in res]
                n.append(i)
                self.helper(n, nums, used, final)
                used[i] = 0
        
    def permute(self, nums):
        final = []
        self.helper([], nums, dict(), final)
        return final
        
