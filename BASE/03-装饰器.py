#简单的装饰器
#简单来说就是A函数对B函数进行操作，返回一个函数，A就是B的装饰器
def some():
    print('小白')
def qwer(func):
    def inner():
        print('*' * 20)
        func()
        print('现在已成大佬')
        print('*' * 20)
    return inner
f = qwer(some)
f()
#----------------------------------------------------------------------------------
#2
def say(age):
    print("I'm %d years old." %age)
def outer(func):
    def inner(age):
        print(age)
        if age<0:
            age = 0
        func(age)
    return inner
say = outer(say)
say(-50)
print('*' * 20)
#或者，outer在前，在say上写@outer就可以了
#-------------------------------------------------------------------------------------
#通用的装饰器
def outer(func):
    def inner(*args,**kwargs):
        print('haha,outer')
        func(*args,**kwargs)
    return inner

@outer
def say(name,age):
    print('{} is {} years old.'.format(name,age))

say('haha',18)
print('*' * 20)
