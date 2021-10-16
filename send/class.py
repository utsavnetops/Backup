class A(object):
    def __init__(self, a):
        self.num = a

    def mul_two(self):
        self.num *= 2


class B(A):
    def __init__(self, a):
        X.__init__(self, a)

    def mul_three(self):
        self.num *= 3


obj = B(4)
print(obj.num)

obj.mul_two()
print(obj.num)

obj.mul_three()
print(obj.num)
