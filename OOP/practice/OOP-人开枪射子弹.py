'''
人开枪射子弹                  或者两个类，人和枪
分析：
类：人
属性：枪
      子弹  num
方法：开枪，子弹没有的话没法开枪了
      上子弹，子弹填满
'''
class Person():
    def __init__(self):
        self.gun = 'AK47'
        self.danjia = 30
    def fire(self):
        if self.danjia != 0:
            print('{}:突，子弹数：{}'.format(self.gun,self.danjia))
            self.danjia -=1
        else:
            print('啊，没子弹了')
    def add(self):
        self.danjia = 30
        print('子弹已装满')

#a = Person()
#for i in range(35):
#    a.fire()
#a.add()
#for i in range(5):
#    a.fire()