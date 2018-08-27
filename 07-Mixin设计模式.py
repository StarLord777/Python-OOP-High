#Mixin设计模式，模块化的思想，扩充多个单一的功能
#基于python支持多继承来实现

class A():
    counts = 0
    def __init__(self):
        A.counts +=1
print(A.counts)
a = A()
print(a.counts)
b = A()
print(b.counts)
