from math import sqrt
class Solution(object):
    def checkPerfectNumber(self, num):
        if num < 2:
            return False
        total = 1
        n = int(sqrt(num))
        for i in range(2, n+1):
            if num % i == 0:
                total += i + num / i
        return total > 1 and total == num
