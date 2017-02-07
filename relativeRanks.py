class Solution(object):
    def findRelativeRanks(self, nums):
        d = dict()
        l = sorted(nums, reverse=True)
        for i in range(len(l)):
            rank = i + 1
            if rank == 1:
                d[l[i]] = 'Gold Medal'
            elif rank == 2:
                d[l[i]] = 'Silver Medal'
            elif rank == 3:
                d[l[i]] = 'Bronze Medal'
            else:
                d[l[i]] = str(rank)
        
        return [d[i] for i in nums] 
