import threading,os,time

num = 100

def get():
    global num          #线程做了global声明，就可以与主进程共享全局变量
    num +=10
    print('{}--{}'.format(threading.current_thread(),num))

if __name__ == '__main__':
    p = threading.Thread(target=get,)

    p.start()
    p.join()

    print('全局变量num={}'.format(num))