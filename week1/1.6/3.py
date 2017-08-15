class A:
    def func(self):
        print('A')


class B:
    def func(self):
        print('B')


class C(A, B):
    pass


class D(B, A):
    pass

c = C()
c.func()

d = D()
d.func()

print(C.mro())