'''
在创建子进程时对全局变量做了一个备份，和主进程中的变量是完全不同的，子进程有自己的储存空间
所以在子进程中修改全局变量是不对主进程起作用的
'''

from multiprocessing import Process
import os

num = 100

def get():
    print('子进程启动')
    global num
    num += 1
    print(num)
    print('子进程结束')


if __name__ == '__main__':
    print('父进程开始')

    p = Process(target=get)
    p.start()
    p.join()

    print('父进程结束{}'.format(num))