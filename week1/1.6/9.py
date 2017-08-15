import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, e):
        self.log(e)
        super(LoggableList, self).append(e)


x = LoggableList()
x.append('s')