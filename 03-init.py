#关于类的__init__方法
class A():
    num = 100
    def __init__(self):
        self.num = 777
    def get_num(self):
        print(self.num, __class__.num)

print(A.num)
a = A()     #对象一被创建，便执行了初始化函数
a.get_num()