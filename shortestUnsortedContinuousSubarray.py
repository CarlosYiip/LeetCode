class Solution(object):
    def findUnsortedSubarray(self, nums):
        largest = -float('inf')
        end = 0
        for i in range(len(nums)):
            largest = max(largest, nums[i])
            if largest > nums[i]:
                end = i
        smallest = float('inf')
        start = 0
        for i in range(len(nums)-1, -1, -1):
            smallest = min(smallest, nums[i])
            if smallest < nums[i]:
                start = i
        if start == end:
            return 0
        return end - start + 1
