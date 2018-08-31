#异常处理略过
'''
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
'''
#-------------------------------------------------------------------
#断言
#基本不用，一种找错误的方法吧
def div(num,div):
    assert (div !=0),'被除数=0'
    return num/div
div(10,0)