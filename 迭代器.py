# A为迭代器
class A(object):
    def __init__(self, n):
        self.n = n
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration


# B为可迭代对象，迭代方法交给A处理
class B(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return A(self.n)
#
#
# a = A(3)
# for i in a:
#     print(i)
# for i in a:
#     print(i)
# iter()
b = B(5)
for i in b:
    print(i)
for i in b:
    print(i)