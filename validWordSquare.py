class Solution(object):
    def validWordSquare(self, words):
        for i in range(len(words)):
            for j in range(len(words[i])):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except IndexError:
                    return False
        return True
