class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        low, high = 1, num
            
        while low < high:
            mid = (low + high) // 2
            if mid ** 2 == num or high ** 2 == num or low ** 2 == num:
                return True
            if mid ** 2 < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
