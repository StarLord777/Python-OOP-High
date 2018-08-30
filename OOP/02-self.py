#类的self
class A():
    def say(self):
        print("self python")
        return 1
    def sayA():
        print("haha")
        return 2

a = A()
a.say()
#print(a.sayA())
#报错
A.sayA()

#含有self的方法可以有对象调用，因为对象调用时自动传入对象本身
#不含self的方法如果被对象调用，传入了参数，会有参数多的错误，只能由类调用

#如果在函数中想使用类的变量，可以使用__class__.变量
class B():
    num = 100
    def get_num(self):
        self.num = 999
        print(self.num,__class__.num)
    def getNum():
        print(__class__.num)

b = B()
b.get_num()
B.getNum()

#b.getNum()
#B.get_num()
# 类只能访问绑定类的方法，对象只能访问含有self的方法