class Solution(object):
    def helper(self, temp, possible_letters, pos, start, N, res):
        if len(temp) == N:
            res.append(''.join(temp))
            return
    
        for j in possible_letters[pos]:
            temp.append(j)
            self.helper(temp, possible_letters, pos+1, start+1, N, res)
            temp.pop()
    
    
    def letterCombinations(self, digits):
        if not digits:
            return []
        d = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        possible_letters = []
        for c in digits:
            possible_letters.append(d[c])
        res = []
        self.helper([], possible_letters, 0, 0, len(digits), res)
        return res
