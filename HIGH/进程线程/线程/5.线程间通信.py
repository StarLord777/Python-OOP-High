'''
线程间的通信采用事件，event，只要控制了事件对象就能控制线程什么时候执行
'''
import threading,os,time

def func():
    event = threading.Event()   #这个地方一般都一定要加括号，实例化对象，类需要加括号
    def run():
        for i in range(1000):
            event.wait()
            event.clear()
            print('you need python')
    threading.Thread(target=run,).start()

    return event            #返回事件对象供变量调用


q = func()                  #q获取了事件对象

while True:
    a = input()
    if a == 'run':
        q.set()