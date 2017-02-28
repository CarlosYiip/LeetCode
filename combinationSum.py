class Solution(object):
    def helper(self, temp, nums, goal, res, start):
        if goal == 0:
            res.append([i for i in temp])
            return
    
        if goal < 0:
            return
    
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.helper(temp, nums, goal-nums[i], res, start)
            start += 1
            temp.pop()
    
    def combinationSum(self, nums, goal):
        res = []
        self.helper([], nums, goal, res, 0)
        return res
