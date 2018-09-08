'''
进程间通信使用队列，队列由父进程创建
'''

from multiprocessing import Queue,Process
import time

def write(queue):
    print('写进程启动')
    for i in range(5):
        queue.put('some{}'.format(i))
        print('我写了')
        time.sleep(1)

def read(queue):
    print('读进程启动')
    while True:
        print('我读到了-----',queue.get(True))
        #q.get(True)可以读队列时阻塞等着，直到有数据，不写也一样，也就是说，默认阻塞等待


if __name__ == '__main__':
    #父进程创建队列，并将引用传递给两个子进程
    queue = Queue()

    pw = Process(target=write,args=(queue,))
    pr = Process(target=read,args=(queue,))

    pw.start()
    pr.start()

    pw.join()
    #pr.join()          pr进程里是个死循环，无法正常结束
    pr.terminate()

    print('父进程结束')
