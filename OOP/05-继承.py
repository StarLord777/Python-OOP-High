#继承
#------------------------------------------------------------
class A():
    name = 'a'
    age = 0
    def get_info(self):
        print(self.name,self.age)
    def __hello(self):
        print('hello,world')
class B(A):
    pass

b = B()
print(b.name,b.age)
b.get_info()
#b不能使用父类的私有方法，__hello

#子类对父类的成员变量和方法进行继承，并可以使用

#每个类都直接或间接继承自   Object类，

#-------------------------------------------------------------
class Person():
    name = 'ren'
    age = 20
    def sleep(self):
        print('sleeping')
class Student(Person):
    def sleep(self):
        Person.sleep(self)
        print("背单词" * Person.age)

s = Student()
s.sleep()

#子类可以通过调用父类的成员变量来实现代码复用
#-----------------------------------------------------------------
class C():
    def __init__(self):
        self.age = 100
class D(C):
    def __init__(self):
        self.name = 'haha'
d = D()
#print(d.age)   当有自己的构造函数时，不再调用父类的，所以出错

#关于继承的构造函数问题，如果子类没有构造函数，则使用父类的，如果子类有，则使用自己的
#此时父类的构造函数无效

print(C.mro())      #[<class '__main__.C'>, <class 'object'>]
#print(C.__mro__)   一样
print(D.mro())      #[<class '__main__.D'>, <class '__main__.C'>, <class 'object'>]

#用来查本身所有的父类以及自身
#------------------------------------------------------------------------

#多继承问题
#python支持多继承
class Man():
    def walk(self):
        print('walking')
class Spider():
    def tosi(self):
        print('tosi')

class SpiderMan(Man,Spider):
    pass

sm = SpiderMan()
sm.tosi()
sm.walk()

#多继承容易引发问题，不过还是功能强大的

#多继承的MRO问题
#以gf代表grandfather，f代表father，s代表son
class gf1():
    pass
class gf2():
    pass
class f1(gf1,gf2):
    pass
class f2(gf2):  #如果这里也是多继承，子类报错,或许是因为爷爷类一样不好排序，真乱
    pass
class s2(f2,f1):
    pass
class s1(f1,f2):
    pass


print(gf2.mro())
print(f1.mro())
print(f2.mro())
print(s1.mro())
print(s2.mro())

#原则上按照继承的括号内的顺序来排序

#---------------------------------------------------------------
