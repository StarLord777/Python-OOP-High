#面向对象的三大特性，继承，封装，多态
#封装
    #对成员变量的访问进行权限控制
    #三个级别
    #   公开的，    public
    #   受保护的，  protected
    #   隐私的，    private
#对于权限的判定
    #位置：类的内部，类的外部，子类

#----------------------------------------------------------------
#隐私属性       前面加两个_      #python解释器会对他进行改名
class A():
    name = 'diff'
    def __init__(self):
        self.__age = 20
        self.qq = 123456
    def get_info(self):
        print(self.name,self.qq,self.__age)

a = A()
print(a.name,a.qq)
#print(a.__age)     私有的不能直接访问
a.get_info()        #私有的可以被内部访问
class Son_of_A(A):
    def get_info2(self):
        print(self.__age)
b = Son_of_A()
print(b.name,b.qq)
b.get_info()#   可以
#b.get_info2()  出错，在子类的方法中无法访问父类的私有变量，继承于父类的方法则没问题

#对于私有变量的修改和访问可以增加getset方法

#如果非要访问私有变量，其实python解释器将变量名改成了_类名__私有变量名
print(a._A__age)
print('*' * 30)
#----------------------------------------------------------------

#受保护的，protected         变量前加一个_就可以
#在类的内部和子类可以访问，外部不行（外部不能访问是告诉程序员，其实也能访问，这是一种约定俗成）
class B():
    b1 = 1
    _b2 = 2
    __b3 = 3
    def get_num(self):
        print(self.b1,self._b2,self.__b3)
class Son_of_B(B):
    def get_num2(self):
        print(self.b1,self._b2)

b = B()
print(b.b1)
print(b._b2)
#print(b.__b3)      不可以
b.get_num()

son = Son_of_B()
print(son.b1)
print(son._b2)

print('*' * 30)
#----------------------------------------------------------------
#公有的，随便访问





















































