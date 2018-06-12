# Author: wangfang

musiclyric = """
[00:00.05]我是
[04:31.08][04:31.09]tom
"""
dict = {}
musiclyricList = musiclyric.splitlines()
print(musiclyricList)
for lrcLine in musiclyricList:
    str1 = lrcLine.split("]")
    for index  in range(len(str1) -1):
        timestr = str1[index][1:]
        print(timestr)
        timelist = timestr.split(":")
        time = float(timelist[0]) * 60 + float(timelist[1])
        print(time)
        dict[time] = str1[-1]
print(dict)

list1 = []
for time1 in dict:
    list1.append(time1)
list1.sort()
print(list1)
time2 = float(input("time:"))
for n in range(len(list1)):
    temptime = list1[n]
    if temptime > time2:
        break
print(dict[list1[n-1]])