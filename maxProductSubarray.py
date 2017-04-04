class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        res = nums[0]
        max_product = [nums[0]]
        min_product = [nums[0]]
        
        for e in nums[1:]:
            l = [max_product[-1]*e, min_product[-1]*e, e]
            a, b = max(l), min(l)
            res = max(a, res)
            max_product.append(a)
            min_product.append(b)
        return res
