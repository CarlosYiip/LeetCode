class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        low, high = 1, x
    
        while low < high:
            mid = (high + low) // 2        
            if mid ** 2 == x or (mid ** 2 < x and (mid + 1) ** 2 > x):
                return mid
            if mid ** 2 > x:
                high = mid
            else:
                low = mid
        return 1
