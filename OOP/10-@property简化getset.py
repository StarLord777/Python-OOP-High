#如果直接把属性暴露出去，直接更改，不能对更改进行限制

#如果用getset方法可以对属性进行限制修改，但是调用稍显麻烦

#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？

#Python内置的@property装饰器就是负责把一个方法变成属性调用的

#------------------------------------------------------------------------------------
#把一个getter方法变成属性，只需要加上@property就可以了，此时，
# @property本身又创建了另一个装饰器@score.setter，负责把一个
# setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作

class Student():
    _score = 99

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,vaule):
        if vaule >100 or vaule<0:
            print('成绩不合法')
        elif not isinstance(vaule,int):
            print('请输入整数')
        else:
            self._score = vaule

s = Student()
print(s.score)  #99
s.score = 60
print(s.score)  #60

s.score = 77.77     #请输入整数
print(s.score)      #60

s.score = 1000      #成绩不合法
print(s.score)      #60

s.score = 100
print(s.score)      #100

#----------------------------------------------------------------------------
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
