



#if语句
#if-else语句
#if-elif-else语句

#格式
'''
if 表达式1:
    语句1
elif 表达式2:
    语句2
elif 表达式3:
    语句3
else:                           #可有可无
    语句4
'''
'''
age = int(input("请输入你的年龄:"))
if age <= 3:
    print("幼儿！")
elif age > 3  and age <= 6:
    print("儿童！")
elif age > 6 and age <= 19:
    print("少年！")
elif age > 19 and age <= 30:
    print("青年")
elif age > 30 and age <= 50:
    print("中年")
elif age >50:
    print("老年")
'''

age = int(input("请输入你的年龄:"))
if age <= 3:
    print("幼儿！")
elif age <= 6:
    print("儿童！")
elif age <= 19:
    print("少年！")
elif age <= 30:
    print("青年")
elif age <= 50:
    print("中年")
elif age >50:
    print("老年")