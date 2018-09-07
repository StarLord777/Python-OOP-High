import doctest
#doctest可以提取注释中的代码执行，还有它严格按照python解释器的输入，测试中文档代码需要加空格

def sub(a,b):
    '''
    求两个数的和
    :param a: 参数一
    :param b: 参数二
    :return: 返回和
    >>> print(sub(6,7)) #print前需要加一个空格
    13
    '''
    return a+b+1


print(sub(5,6))

doctest.testmod()