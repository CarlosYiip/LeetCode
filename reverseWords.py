class Solution(object):
    def reverseWords(self, s):
        return ' '.join([c[::-1] for c in s.split(' ')])
