from multiprocessing import Process
import time,os

class MyPrecess(Process):
    def __init__(self,name):
        Process.__init__(self)          #Process类的init函数一定要执行，否则报错
        self.name = name

    def run(self):
        start = time.time()
        print('Process--{}--{}'.format(self.name,os.getpid()))
        time.sleep(2)
        end = time.time()
        print('进程{}结束,耗时{}'.format(os.getpid(),end-start))


if __name__ == '__main__':
    p = MyPrecess('test')
    q = MyPrecess('qq')
    p.start()
    q.start()
