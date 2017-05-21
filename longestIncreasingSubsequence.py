Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        tails = len(nums) * [0]
        tails[0] = 1
        for i in range(len(nums)):
            update = 1
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    update = max(tails[j] + 1, update)
            tails[i] = update
        return max(tails)
