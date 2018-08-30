#1默认参数
def getnum(num = 6):
    print(num)

getnum(7)
getnum()
#------------------------------------------------------------------------------
#2不定长参数
#可以直接传值，是tuple类型，可以对值进行遍历
#可以传键值对，是dict类型，可以对键值对进行遍历
def get_some(a,*args,**kwargs):
    print(a,type(a))
    print(args,type(args))
    print(kwargs,type(kwargs))
    for i in args:
        print(i,end=' ')
    print()
    for i,j in kwargs.items():
        print(i,j,end=' ')

get_some(5,9,'haha',q=77,w=88,e=99)
#5 <class 'int'>
#(9, 'haha') <class 'tuple'>
#{'q': 77, 'w': 88, 'e': 99} <class 'dict'>
#9 haha
#q 77 w 88 e 99