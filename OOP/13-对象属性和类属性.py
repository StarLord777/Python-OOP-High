#对象属性和类属性
class A():
    #在这里定义的属性是类属性，如果没有同名的对象属性，则调用类属性
    name = 'a'
    def __init__(self,name):
        self.name = name
        self.haha = 1

a = A('haha')
print(a.name)
#类只能调用类属性
#print(A.haha)
print(A.name)
del a.name
print(a.name)

#注意一般不要将对象属性与类属性同名，否则对象属性将屏蔽掉类属性

