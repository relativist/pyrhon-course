import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, value):
        self.log(value)
        super(LoggableList, self).append(value)

l = LoggableList()
l.append('1')
l.append('2')
print(l)
