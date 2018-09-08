'''
进程多的话,创建一个进程池，统一管理
可以设置进程池的存储数量
'''

from multiprocessing import Process,Pool
import time
import os

def run(num):
    print('{}开始'.format(num))
    time.sleep(3)
    print('进程开始，进程结束-{}--{}'.format(num,os.getpid()))

if __name__ == '__main__':
    print('主进程开始---{}'.format(os.getpid()))

    p_pool = Pool(4)        #并行执行的个数

    for i in range(6):
        p_pool.apply_async(run,(i,))


    p_pool.close()
    p_pool.join()           #必须调用.close后才能join
    print('父进程结束')