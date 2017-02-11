class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        p = 1
        for i in nums:
            res.append(p)
            p *= i
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res
