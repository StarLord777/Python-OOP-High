#高阶函数sorted

#普通排序
list1 = [9,5,4,1,7]
list2 = sorted(list1)
list3 = sorted(list1,reverse=True)
print(list2)
print(list3)
print('*'*20)

#绝对值排序---------------------------------
l1 = [-5,3,-1,7,9,-4]
l2 = sorted(l1,key=abs)
print(l2)

#key可以接受函数作为规则，可以自定义规则

def alen(str):
    return len(str)

a1 = ['haha','starlord','qq','l','life is short']
a2 = sorted(a1,key=alen)
print(a2)