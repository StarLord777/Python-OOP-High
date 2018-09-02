#动态添加属性不用说，动态添加方法需要引入模块

from types import MethodType

class A():
    pass

a = A()

a.name = 'haha'
a.age = 20
print(a.name,a.age)

def say(self):
    print(self.name,':',self.age)

a.say = MethodType(say,a)

a.say()