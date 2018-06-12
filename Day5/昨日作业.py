# Author: wangfang
#10:30:29

#str = "10:30:29"
#print(str.split(":"))
str = input("input:")
list = str.split(":")
hours = int(list[0])
mins = int(list[1])
second = int(list[2]) + 1
if second == 60:
    mins += 1
    second = 0
    if mins == 60:
        hours += 1
        mins = 0
        if hours == 24:
            hours = 00
print("%d:%d:%d" %(hours,mins,second))

