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
