'''
UTC（世界协调时间）：世界标准时间，对中国来说是UTC+8
DST（夏令时）：是一种节约能源而人为规定制度，在夏季调快一个小时

时间的表示方式：
    1丶时间戳：以整形或浮点型表示时间的一个以秒为单位的时间间隔.这个时间间隔的基础值是从1970年1月1日开始算起
    2丶元组：一种python的数据结构表示,这个元组有9个整形内容
        year
        month
        day
        hours
        minutes
        seconds
        weekday
        julia day
        flag
    3丶格式化字符串
        %Y
        %m
        %d
'''

import time
#time.time()   返回当前时间的时间戳，浮点数形式，不需要参数
time1 = time.time()
print(time1)

#time.gmtime()  将时间戳转为UTC时间元组
time2 = time.gmtime(time1)
print(time2)

#time.localtime 将时间戳转为本地时间元组
time3 = time.localtime(time1)
print(time3)

#    time.mktime()  将本地时间元组转为时间戳
time4 = time.mktime(time3)
print(time4)

#time.asctime()   将本地时间元组转为字符串
time5 = time.asctime(time3)
print(time5)

#time.ctime()   将时间戳转为字符串
time6 = time.ctime(time1)
print(time6)

#time.strftime()  将时间元组转换成给定格式的字符串,参数2为时间元组,如果没有参数2,默认转当前时间
time7 = time.strftime("%Y-%m-%d %H:%M:%S",time3)
print(time7)
print(type(time7))

# time.strptime() 将时间字符串转为时间元组
time7 = time.strptime(time7,"%Y-%m-%d %X")
print(time7)


#time.sleep() 延迟一个时间，给整形或者浮点型
time.sleep(1)

#time.clock() 返回当前程序的cpu执行执行
#unix始终返回全部的运行时间
#windows从第二次开始，都是以第一次调用此函数的开始间隔作为基数

time8 = time.clock()
time.sleep(1)
time9 = time.clock()
print(time9)