import os
#递归
d = 'E:\\'
def get_all(menu,sp=''):
    dirs = os.listdir(menu)
    sp +='  '
    for i in dirs:
        absd = os.path.join(menu, i)
        if os.path.isdir(absd):
            print(sp+'目录：',i)
            get_all(absd,sp)
        else:
            print(sp+'文件：',i)

#get_all('..')
#----------------------------------------------------------------------------------
#利用栈遍历目录
import pythonStack
def get_all_by_stack(path,sp=''):
    stack = pythonStack.Stack()
    stack.push(path)
    while not stack.is_empty():
        a = stack.pop()
        dirs = os.listdir(a)
        for i in dirs:
            if os.path.isdir(os.path.join(a,i)):
                print(sp,'目录：',i)
                stack.push(os.path.join(a,i))
            else:
                print(sp,'文件：',i)

get_all_by_stack('..')