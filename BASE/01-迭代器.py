from collections import Iterable,Iterator

#可迭代对象
#字符串，列表，元组，字典，集合
a = [1,2,3,4]
b = isinstance(a,Iterable)      #True   可迭代对象
print(b)

#迭代器
#可以for循环，可以被next（）调用，被next（）调用，一直返回下一个值，直到出现StopIteration错误
print(isinstance(a,Iterator))   #FALSE  不是一个迭代器
a = (x*x for x in range(2))
print(type(a))                  #<class 'generator'>
print(isinstance(a,Iterator))   #true  是迭代器
print(next(a))
print(next(a))
#print(next(a))              报错 StopIteration


#将列表，字符串，字典，元组等转换成迭代器
print('*'*20)
a = [5,4,3]
a = iter(a)
print(isinstance(a,Iterator))
print(next(a))
