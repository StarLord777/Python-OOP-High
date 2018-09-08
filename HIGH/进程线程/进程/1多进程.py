'''
一个任务就是一个进程，程序启动就是一个进程

os.getpid   获取当前进程号
os.getppid  获取父进程号



'''
import multiprocessing
from time import sleep
import os

def loop(str='python'):
    while True:
        print('{}-----{}-{}'.format(str,os.getpid(),os.getppid()))
        sleep(1)
if __name__ == '__main__':
    print('这是主进程，启动{}-{}'.format(os.getpid(),os.getppid()))
    p = multiprocessing.Process(target=loop)
    q = multiprocessing.Process(target=loop,args=('life is short,you need python',))

    q.start()
    p.start()
