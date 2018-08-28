#如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student():
    __slots__ = ('name','age')

s = Student()
#s.name     报错，因为此时没有
s.name = 'xiaoming'
print(s.name)       #正确
#s.haha = 'haha'    报错，这个属性不被允许
s.age = 99
print(s.age)

#----------------------------------------------------------------------------
#__slots__设置对子类无效

class S(Student):
    pass

son = S()
son.age = 99    #可以
son.qwer = 'qwer'   #也可以
print(son.qwer)

#如果在子类中也定义了__slots__，那么子类允许绑定的属性就是子类的加上父类的__slots__

class Test(Student):
    __slots__ = ('score')

t = Test()
t.age = 99
t.name = 'haha'
t.score = 666
t.tt = 88       #这个就会报错

