'''
两个线程之间的调度，采用  condition，发信号的方式
'''
import threading,time,os

cond = threading.Condition()

def run1():
    with cond:
        for i in range(0,10,2):
            print('{}-------{}'.format(threading.current_thread(),i))
            cond.wait()             #执行完一步后等待
            cond.notify()           #并发送信号，让其他人执行

def run2():
    with cond:
        for i in range(1,10,2):
            print('{}-------{}'.format(threading.current_thread(),i))
            cond.notify()           #上面withcond接收到信号执行，到这里发送信号，自己等待
            cond.wait()

if __name__ == '__main__':
    q = threading.Thread(target=run1,)
    p = threading.Thread(target=run2,)

    q.start()
    p.start()
