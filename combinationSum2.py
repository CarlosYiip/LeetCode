class Solution(object):
    def helper(self, temp, nums, goal, start, res):
        if goal == 0:
            res.append([i for i in temp])
            return
    
        if goal < 0:
            return
    
        for i in range(start, len(nums)):
        
            if i > start and nums[i] == nums[i-1]:# Key point!
                continue
            # Skip the element when it appeared before in the previous completed path
            
            temp.append(nums[i])
            self.helper(temp, nums, goal-nums[i], i+1, res)
            temp.pop()
    
    def combinationSum2(self, nums, goal):
        nums.sort()
        res = []
        self.helper([], nums, goal, 0, res)
        return res
