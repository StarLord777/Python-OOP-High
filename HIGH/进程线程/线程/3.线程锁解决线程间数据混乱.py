'''
变量要互斥用      加锁


可以使用
with lock:
    pass
自动加锁解锁
'''
import threading
lock = threading.Lock()

num =100
def get(n):
    global num
    for i in range(1000000):
        #加锁
        lock.acquire()
        num += n
        num -= n
        lock.release()


if __name__ == '__main__':
    print('主进程启动')

    p = threading.Thread(target=get,args=(6,))
    q = threading.Thread(target=get,args=(9,))

    p.start()
    q.start()
    print(num)      #不加锁结果可能不一样，需要互斥用



