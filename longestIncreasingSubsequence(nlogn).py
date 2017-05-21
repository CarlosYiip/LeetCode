class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        res = [nums[0]]
        for i in nums[1:]:
            if i > res[-1]:
                res.append(i)
            else: 
                if len(res) == 1:
                    res[-1] = i
                else:
                    if i <= res[0]:
                        res[0] = i
                    else:
                        lo, hi = 0, len(res)
                        while lo <= hi:
                            mid = (lo + hi) // 2
                            if res[mid] >= i and res[mid-1] < i:
                                res[mid] = i
                                break
                            elif res[mid] >= i:
                                hi = mid
                            else:
                                lo = mid
        return len(res)
