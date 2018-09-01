#time   库
'''
时间的表示形式：
时间戳：指格林威治时间1970年01月01日00时00分00秒起至现在的总秒数。
元组  ：九个内容（tm_year、tm_mon、tm_mday、tm_hour、tm_min、tm_sec、tm_wday、tm_yday、tm_isdst）
格式化字符串
'''
#------------------------------------------------------------------------------
import time
#返回当前时间戳
print(time.time())
#从1970年到现在大约过去的秒数
print(((2018-1970)*365+9*30)*24*60*60)
print('差不多')
#获取UTC时间，元组形式
print(time.gmtime())
#获取本地时间     UTC+8
print(time.localtime())
#将本地时间转换为时间戳
print(time.mktime(time.localtime()))

#字符串形式
print(time.asctime())   #将元组格式转换为字符串
print(time.ctime())     #将时间戳格式转换为字符串

#格式化字符串输出，
f = time.strftime("%Y-%m-%d %H:%M:%S")
print(f)                                        #将时间元组转换为字符串
print(time.strptime(f,"%Y-%m-%d %H:%M:%S"))    #将时间字符串转换为元组，不过得给他格式

#--------------------------------------------------------------------------
import datetime
#datetime   是对time进行了封装
print(datetime.datetime.now())

#日历模块---------------------------------------------------------------------
import calendar

#print(calendar.calendar(2018)) 打印一年的日历
#print(calendar.month(2018,9))   #打印一个月的日历

#判断闰年
print(calendar.isleap(2008))