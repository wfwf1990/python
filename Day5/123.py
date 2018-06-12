# Author: wangfang
dict = {}
musiclyric = """
[00:00.05]我是
[04:31.08][04:31.09]tom
"""
str0 = musiclyric.strip()
str1 = str0.splitlines()
for i1 in str1:
    str2 = i1.split("]")
    print(str2)
    for i2 in range(len(str2)-1):
        time0 = str2[i2][1:]
        time1 = time0.split(":")
        #print(time1)
        time2 = float(time1[0]) * 60 + float(time1[1])
        print(time2)
        dict[time2] = str2[-1]
print(dict)

list1 = []
for i3 in dict:
    list1.append(i3)
list1.sort()
print(list1)

inputtime = float(input("time"))
for i4 in range(len(list1)):
    nowtime = list1[i4]
    if inputtime < nowtime:
        break
print(dict[list1[i4]])
