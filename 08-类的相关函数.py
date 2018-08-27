#检测一个类是否是另一个的子类
class A():
    name = None
    age = 20
class A1(A):
    pass
class B():
    pass
print(issubclass(A1,A))
print(issubclass(B,A))
print(issubclass(A1,object))
print('*' *20)
#---------------------------------------------------------------
#检测一个对象是否是一个类的实例
a = A1()
b = B()
print(isinstance(a,A1))
print(isinstance(a,A))
print(isinstance(a,object))
print(isinstance(b,A))
print('*' * 20)

#-----------------------------------------------------------------
#检测一个类是否有该成员变量
a = A()
print(hasattr(a,"age"))
print(hasattr(a,"ahha"))
#取出，删除，赋值
print(setattr(a,"age",100))
print(getattr(a,"age"))
delattr(a,"name")
#a.name 此时报错
print('*' * 20)
#-------------------------------------------
#dir    获取成员列表
