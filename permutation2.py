class Solution(object):
    def helper(self, temp, nums, res, used):
        if len(temp) == len(nums):
            res.append([i for i in temp])
            return
    
        for i in range(len(nums)):
    
            '''when a number has the same value with its previous,
               we can use this number only if his previous is used.'''
            if i>0 and nums[i-1]==nums[i] and not used[i-1]:
                continue
            
            if i not in used or used[i] == 0:
                used[i] = 1
                temp.append(nums[i])
                self.helper(temp, nums, res, used)
                temp.pop()
                used[i] = 0
    
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        self.helper([], nums, res, dict())
        return res
