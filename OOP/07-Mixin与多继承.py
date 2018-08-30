#多继承
#预防类过多，分类太细，后面会成指数级增长
#可以不细分，而添加功能模块
#正确的做法是采用多重继承
class Animal(object):
    pass
# 大类:
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
# 各种动物:
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
#现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable):
    pass

dog = Dog()
dog.run()           #Running...

#通过多重继承，一个子类就可以同时获得多个父类的所有功能

#--------------------------------------------------------------------------------------
#Mixin设计模式，模块化的思想，扩充多个单一的功能
#基于python支持多继承，动态继承来实现

#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了
# 继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

#为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。



