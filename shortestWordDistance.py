class Solution(object):
    def helper(self, words, word1, word2):
        dis = float('inf')
        word1Index = None
        word2Index = None
        for i in range(len(words)):
            if words[i] == word1:
                if word2Index == None:
                    word1Index = i
                    continue
                else:
                    if abs(i - word2Index) < dis:
                        word1Index = i
                        dis = abs(i - word2Index)
            elif words[i] == word2:
                if word1Index == None:
                    word2Index = i
                    continue
                else:
                    if abs(i - word1Index) < dis:
                        word2Index = i
                        dis = abs(i - word1Index)
        return dis
        
    def shortestDistance(self, words, word1, word2):
        return min(self.helper(words, word1, word2), self.helper(words[::-1], word1, word2))
