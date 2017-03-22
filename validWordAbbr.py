import re
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        n = len(word)
        pattern = []
        prev_is_digit, running_sum, total = False, 0, 0
        for c in abbr:
            if c.isdigit():
                if not prev_is_digit:
                    if c == '0':
                        return False
                    running_sum = int(c)
                    prev_is_digit = True
                else:
                    running_sum = running_sum * 10 + int(c)
            else:
                prev_is_digit = False
                if running_sum == 0:
                    pattern.append(c)
                    total += 1
                else:
                    pattern.append('.{')
                    pattern.append('{}'.format(running_sum))
                    pattern.append('}') 
                    pattern.append(c)
                    total += running_sum + 1
                    running_sum = 0
        if running_sum:
            pattern.append('.{')
            pattern.append('{}'.format(running_sum))
            pattern.append('}')
            total += running_sum
        pattern = ''.join(pattern)
        
        if n != total:
            print(n, total, pattern)
            return False
        
        if re.match(pattern, word):
            return True
        return False
