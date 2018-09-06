#高阶函数filter
'''
参数：fn,lst
作用：用于过滤序列，根据函数返回TRUE还是FALSE决定是否保留该序列
'''

a = range(20)
def fn(x):
    if x%2==0:
        return False
    else:
        return True

b = filter(fn,a)
print(list(b))

