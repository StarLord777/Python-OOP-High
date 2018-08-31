import os
#递归
d = 'E:\\'
def get_all(menu):
    dirs = os.listdir(menu)
    for i in dirs:
        absd = os.path.join(menu, i)
        if os.path.isdir(absd):
            print('目录：',i)
            get_all(absd)
        else:
            print('文件：',i)

#get_all(d)