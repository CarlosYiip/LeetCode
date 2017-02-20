class Solution(object):
    def maxSubArray(self, nums):
        maxSumSoFar, sumSoFar = nums[0], nums[0]
        for i in range(1, len(nums)):
            sumSoFar = max(sumSoFar + nums[i], nums[i])
            maxSumSoFar = max(maxSumSoFar, sumSoFar)
        return maxSumSoFar
