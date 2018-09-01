'''
析构函数：
在类的对象被释放（程序结束或者对象被释放掉）
时，调用该函数，执行一些功能
'''
class A():
    def say(self):
        print('hello,python')
    def __del__(self):
        print('该对象被释放了')

a = A()
a.say()
del a
print('--------------------------------')