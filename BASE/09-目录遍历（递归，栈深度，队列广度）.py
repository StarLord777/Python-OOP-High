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
from queue import LifoQueue     #后进先出是为栈
def get_all_by_stack(path,sp=''):
    stack = LifoQueue()
    stack.put(path)
    while not stack.empty():
        a = stack.get()
        dirs = os.listdir(a)
        for i in dirs:
            if os.path.isdir(os.path.join(a,i)):
                print(sp,'目录：',i)
                stack.put(os.path.join(a,i))
            else:
                print(sp,'文件：',i)

#get_all_by_stack('..')
#-----------------------------------------------------------------------------
#队列
from queue import Queue     #先进先出是为队列
def get_all_by_queue(path):
    queue = Queue()
    queue.put(path)
    while not queue.empty():
        base = queue.get()
        dirs = os.listdir(base)
        for i in dirs:
            if os.path.isdir(os.path.join(base,i)):
                print('目录：',i)
                queue.put(os.path.join(base,i))
            else:
                print('文件',os.path.join(base,i))

get_all_by_queue('..')
