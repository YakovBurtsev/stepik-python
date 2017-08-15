class ExtendedStack(list):
    def sum(self):
        if len(self) > 1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 + top2)

    def sub(self):
        if len(self) > 1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 - top2)

    def mul(self):
        if len(self) > 1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 * top2)

    def div(self):
        if len(self) > 1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 // top2)


x = ExtendedStack()
x.extend([1, 2, 3])
x.sum()
print(x)
x.sub()
print(x)
x.extend([2, 2])
x.mul()
print(x)
