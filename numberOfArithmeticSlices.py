class Solution(object):
    def numberOfArithmeticSlices(self, A):
        total = 0
        count = 1
        for i in range(len(A)-2):
            diff1 = A[i+1] - A[i]
            diff2 = A[i+2] - A[i+1]
            if diff1 == diff2:
                count += 1
            elif count >= 2:
                total += (1 + count-1) * (count-1) // 2
                count = 1
            
        if count >= 2:
            total += (1 + count-1) * (count-1) // 2
            
        return total
