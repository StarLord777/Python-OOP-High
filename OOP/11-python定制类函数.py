#__str__返回字符串   __repr__返回系统调试字符串
class A():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "class:A name:{}".format(self.name)

a = A('haha')
print(A('666'))
print(a)

#----------------------------------------------------------------
#__iter__   返回一个可以迭代的对象
class Fib():
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration
        return self.a

for i in Fib():
    print(i)

#-----------------------------------------------------------------------------
#__call__直接对类实例进行调用
class Call():
    def __call__(self, *args, **kwargs):
        print("直接调用了类")

c = Call()
c()