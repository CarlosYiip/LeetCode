class TwoSum(object):
    def __init__(self):
        self.nums = dict()
    
    def add(self, number):
        if number not in self.nums:
            self.nums[number] = 1
        else:
            self.nums[number] += 1
        
    def find(self, value):
        for a in self.nums:
            b = value - a
            if b in self.nums:
                if a == b:
                    if self.nums[a] > 1:
                        return True
                else:
                    return True
        return False
