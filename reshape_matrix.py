class Solution(object):
    def matrixReshape(self, nums, r, c):
        if r * c > len(nums) * len(nums[0]):
            return nums
        new_matrix = [[None for j in range(c)] for i in range(r)]
        
        a, b = 0, 0
        for i in range(r):
            for j in range(c):
                new_matrix[i][j] = nums[a][b]
                b += 1
                if b == len(nums[a]):
                    b = 0
                    a += 1
        return new_matrix
