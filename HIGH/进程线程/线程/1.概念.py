'''
在一个进程的内部，需要实现多任务，就需要运行多个子任务，即线程

线程通常叫做轻型的进程，共享内存空间，并发执行

模块：
_thread:    接近底层，封装C语言模块
threading:  高级，对_thread进行封装

任何一个进程都会默认启动一个线程，这个线程称为主线程
'''

import threading,os,time

def get():
    print('haha---{}--{}'.format(threading.current_thread(),threading.current_thread().name))



if __name__ =='__main__':
    print('主进程启动，{}'.format(os.getpid()))
    print('主线程--{}'.format(threading.current_thread()))

    #创建子线程
    p = threading.Thread(target=get,name='th1')
    q = threading.Thread(target=get,name='th2')

    p.start()
    q.start()

    #最好都等待线程结束
    p.join()
    q.join()

    print('主线程结束')


