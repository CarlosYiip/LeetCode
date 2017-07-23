class Solution(object):
    def maxSubArray(self, nums):
        if all([i <= 0 for i in nums]):
            return max(nums)
        res = [0]
        for i in nums:
            if i + res[-1] < 0:
                res.append(0)
            else:
                res.append(i + res[-1])
        return max(res)
