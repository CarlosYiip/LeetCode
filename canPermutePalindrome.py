class Solution(object):
    def canPermutePalindrome(self, s):
        counter = dict()
        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        
        foundOdd = False
        for c in counter:
            if counter[c] % 2 != 0:
                if foundOdd:
                    return False
                else:
                    foundOdd = True
        return True
