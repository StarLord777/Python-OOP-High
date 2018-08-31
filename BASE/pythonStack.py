#python实现栈，特点，先进后出
class Stack():
    def __init__(self):
        self.list = []
    #返回栈的长度
    def getsize(self):
        return len(self.list)
    #入栈
    def push(self,a):
        self.list.append(a)
    #出栈
    def pop(self):
        return self.list.pop()
    #判断是否为空栈
    def is_empty(self):
        return self.list == []