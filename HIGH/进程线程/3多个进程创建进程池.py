'''
进程多的话,创建一个进程池，统一管理
可以设置进程池的存储数量
'''

from multiprocessing import Process,Pool
import time
import os

def run(num):
    print('进程开始，进程结束-{}--{}'.format(num,os.getpid()))


if __name__ == '__main__':
    print('主进程开始---{}'.format(os.getpid()))

    p_pool = Pool()

    for i in range(5):
        p_pool.apply(run,(i,))


