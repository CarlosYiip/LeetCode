class Solution(object):
    def helper(self, temp, nums, k, goal, start, res):
        if len(temp) == k and goal == 0:
            res.append([i for i in temp])
            return
        
        if goal < 0:
            return
        
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.helper(temp, nums, k, goal-nums[i], i+1, res)
            temp.pop()
    
    def combinationSum3(self, k, n):
        nums = [i for i in range(1, 10)]
        res = []
        self.helper([], nums, k, n, 0, res)
        return res
