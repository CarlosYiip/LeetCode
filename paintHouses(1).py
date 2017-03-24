class Solution(object):
    def minCost(self, costs):
        if not costs:
            return 0
        n, c = len(costs), len(costs[0])
        matrix = [[0 for j in range(c)] for i in range(n)]
        
        for i in range(n):
            for j in range(c):
                if i == 0:
                    matrix[i][j] = costs[i][j]
                else:
                    min_of_prev_row = float('inf')
                    for k in range(c):
                        if k == j:
                            continue
                        min_of_prev_row = min([min_of_prev_row, matrix[i-1][k]])
                    matrix[i][j] = costs[i][j] + min_of_prev_row
        return min(matrix[-1])
