class Logger(object):
    def __init__(self):
        self.d = dict()
        
    def shouldPrintMessage(self, timestamp, message):
        if message in self.d:
            prev = self.d[message]
            if timestamp - prev >= 10:
                self.d[message] = timestamp
                return True
            else:
                return False
        else:
            self.d[message] = timestamp
            return True



logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2,"bar"))
print(logger.shouldPrintMessage(3,"foo"))
print(logger.shouldPrintMessage(8,"bar"))
print(logger.shouldPrintMessage(10,"foo"))
print(logger.shouldPrintMessage(11,"foo"))
