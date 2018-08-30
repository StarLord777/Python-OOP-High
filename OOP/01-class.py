#类
class Student():
    name = None
    age = 18
    def __init__(self):
        self.hobby = 'python'
    def do_homework(self):
        print("This student is doing homework.")

#通过默认内置变量检查类和对象的所有成员变量
print(Student)
#<class '__main__.Student'>     类
xiaoming = Student()
print(xiaoming)
#<__main__.Student object at 0x0000024B33620B70>    对象

print(Student.__dict__)
#{'__module__': '__main__', 'name': None, 'age': None,
# 'do_homework': <function Student.do_homework at 0x00
# 0001B9C74F2AE8>, '__dict__': <attribute '__dict__' of
#  'Student' objects>, '__weakref__': <attribute '__weak
# ref__' of 'Student' objects>, '__doc__': None}
print(xiaoming.__dict__)
#{'hobby': 'python'}        通过初始化的变量可以显示出来
xiaoming.name = 'xiaoming'
xiaoming.age = 20
print(xiaoming.__dict__)
#{'hobby': 'python', 'name': 'xiaoming', 'age': 20}     这就有了

class a(Student):
    test = 'haha'
print(a.__dict__)
#{'__module__': '__main__', 'test': 'haha', '__doc__': None}

#实例的__dict__仅仅包含与该实例有关的属性
#类的dict包含所有实例共享的变量和函数，且并不包含父类的属性

#创建对象时，如果不初始化，对象为空，调用属性是引用类的属性
#如果对属性赋值，或者建立新的属性，则在对象内部创建，此时不再调用类的相关属性