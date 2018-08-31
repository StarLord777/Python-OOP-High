#OS模块
import os
#os.system('notepad')   执行系统命令，功能强大，用的较多

print(os.name)  #返回操作系统标志
print(os.environ)#返回系统环境变量

print(os.curdir)#返回当前目录
print(os.getcwd())  #获取当前工作路径，绝对路径
print(os.listdir()) #返回指定目录下所有文件列表

#os.mkdir('kkk')
#os.rmdir('kkk')        #创建删除文件夹
#os.rename()
#os.remove('1.txt')

print(os.path.curdir)
print(os.path.abspath('.'))



