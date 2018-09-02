'''
人一个类，枪一个类
'''
class Gun():
    def __init__(self):
        self.danjia = 30
        print('你现在拥有了一把枪')
    def fire(self):
        if self.danjia != 0:
            print('AK47:突，子弹数：{}'.format(self.danjia))
            self.danjia -=1
        else:
            print('啊，没子弹了')
    def add(self):
        self.danjia = 30
        print('子弹已装满')

class Person():
    def __init__(self):
        print('现在我还没有枪')
    def getGun(self):
        self.gun = Gun()
    def fire(self):
        self.gun.fire()
    def add(self):
        self.gun.add()

a = Person()
a.getGun()
for i in range(33):
    a.fire()

a.add()
for i in range(4):
    a.fire()
