class Solution(object):
    def minMoves2(self, nums):
        m = sorted(nums)[len(nums) // 2]
        return sum([abs(i - m) for i in nums])
