class MovingAverage(object):
    def __init__(self, s):
        self.capacity = s
        self.size = 0
        self.data = []
        self.total = 0.0

    def next(self, val):
        self.size += 1.0
        if self.size <= self.capacity:
            self.data.append(val)
            self.total += val
            return float(self.total / self.size)
        else:
            self.size -= 1.0
            self.total -= self.data.pop(0)
            self.data.append(val)
            self.total += val
            return float(self.total / self.size)
