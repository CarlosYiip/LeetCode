class Solution(object):
    def minDistance(self, word1, word2):
        word1 = '.' + word1
        word2 = '.' + word2
        
        matrix = [[0 for i in range(len(word1))] for j in range(len(word2))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0 and j == 0:
                    matrix[i][j] = 0
                
                if i == 0:
                    insert = j
                else:
                    insert = matrix[i-1][j] + 1
                if j == 0:
                    delete = i
                else:
                    delete = matrix[i][j-1] + 1
        
                if word1[j] == word2[i]:
                    if i != 0 and j != 0:
                        cost = matrix[i-1][j-1]
                    else:
                        cost = float('inf')
                else:
                    if i != 0 and j != 0:
                        cost = matrix[i-1][j-1] + 1
                    else:
                        cost = float('inf')
                    
                matrix[i][j] = min(insert, delete, cost)
                
        return matrix[-1][-1]
