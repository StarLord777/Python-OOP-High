#map函数
#原型map(fn,lsd)      第一个参数是函数，第二个参数是序列
#作用：将传入的函数依次作用于序列的每一个元素，并把结果作为新的Iterator返回

def chr2int(str):
    return int(str)

ls = ['5','9','8','7','4','1']

a = map(chr2int,ls)
#print(list(a))             [5, 9, 8, 7, 4, 1]
for i in a:
    print(i,type(i))        #单个元素全部为int

#将ASCII字符转换为对应的编码
c = map(ord,('a','D','E','z'))
print(list(c))
#将数字转换为ASCII字符
b = map(chr,[65,68,75,97,104])
print(list(b))

#-----------------------------------------------------------------------------------------------
#reduce(fn,ls)
#作用：函数作用在序列上，函数有两个参数，函数结果再与后一个序列中的元素做运算
#reduce(f,[a,b,c,d])
#相当于：f(f(f(a,b),c),d)

#求一个序列的和
from functools import reduce
def add(a,b):
    return a+b
ls = [1,2,3,4,5,6,7,8,9,10]
a = reduce(add,ls)
print(a)

#mapreduce合用
def str2int(a):
    def fn(a,b):
        return a*10+b
    def toint(chr):
        return int(chr)
    return reduce(fn,map(toint,a))

a = ['5','8','9','6','1','7']
b= str2int(a)
print(b)