#pickle 数据持久性模块
import pickle
list = [1,2,8,7,9,'hello,python']
dict = {1:2,'haha':list}

with open('1.txt','wb+') as f:
    pickle.dump(list,f)
    pickle.dump(dict,f)
with open('1.txt','rb') as f:
    a = pickle.load(f)
    b = pickle.load(f)
    print(a)
    print(b)

#一次dump进去一个，一次也只能load出来一个，需要遍历load
#当然，这东西对于长的列表字典比较友好

