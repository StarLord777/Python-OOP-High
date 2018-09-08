'''
threadlocal  为每一个线程创建一片内存空间

作用：为每个线程绑定一个数据库，HTTP请求，用户身份等等
'''
import threading,os
import random

local = threading.local()

num = 100

def get(num):
    local.x = num
    local.x += random.random()*1000
    print('{}-----{}'.format(threading.current_thread(),local.x))


if __name__ == '__main__':

    p = threading.Thread(target=get,args=(num,))
    q = threading.Thread(target=get,args=(num,))

    p.start()
    q.start()
    print(num)