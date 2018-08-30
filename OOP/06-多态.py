#多态也没什么好说的

#多态指的是一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）

#--------------------------------------------------------------
#多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同
# 内容的函数。在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，
# 不同的对象在接收时会产生不同的行为（即方法）。也就是说，每个对象可以用自己的方式
# 去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。

#多态性，定义统一的接口，进行调用，产生不同的结果
class Person():
    def info(self):
        print("person")
class Teacher(Person):
    def info(self):
        print("teacher")
class Student(Person):
    def info(self):
        print("student")

def get_info(CLASS):
    CLASS.info()

p = Person()
t = Teacher()
s = Student()

get_info(p)
get_info(t)
get_info(s)