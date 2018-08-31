#这个东西好像不常用
a = int('1010',base=2)#按照2进制转换，默认是10进制
print(a)

#可以
def int2(str):
    return int(str,base=2)

#还可以
import functools
int_2 = functools.partial(int,base=2)
print(int_2('111000'))

