class Solution(object):
    def uniquePaths(self, m, n):
        matrix = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        return matrix[-1][-1]