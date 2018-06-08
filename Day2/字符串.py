'''
什么是字符串：
    字符串是以单引号或双引号括起来的任意文本
    'abc'  "ABC" "123"
字符串不可变
'''

#创建字符串
str1 = "Hello World!"


'''
字符串运算
'''
#字符串连接
str2 = "Hello "
str3 = "World!"
str4 = str2 + str3
print("str4 = ", str4)


#输出重复字符串
str5 = "good"
str6 = str5 * 3
print("str6 = ", str6)

#访问字符串中的某一个字符
#通过索引下标查找字符,索引从0开始
str7 = "Hello World!"
print(str7[6])
#str7[6] = "M"           #字符串不可变
#print("str7 = ", str7)

#截取字符串中的一部分
str7 = "Hello World!"
#从给定下标处开始截取到给定下标之前
str8 = str7[2:6]
#从头截取到给定下标之前
str9 = str7[:6]
#从给定下标处开始截取到结尾
str10 = str7[6:]
print("str8 = ", str8)
print("str10 = ", str10)


#判断字符串是否在变量的值中
str11 = "Hello World!"
print("Hello" in str11)
print("hello1" not in str11)

#格式化输出
str12 = "Hello World!"
num1 = 12
f1 = 12.1236
#%s %d %f 都是占位符
print("str12 = %s , num1 = %d , f1 = %f" % (str12,num1,f1))
#                                         精确小数点后3位,会四舍五入
print("str12 = %s , num1 = %d , f1 = %.3f" % (str12,num1,f1))


# 转义字符  \
#将一些字符转换成有特殊含义的字符
# \n 换行符
print("str12 = %s\nnum1 = %d\nf1 = %.3f" % (str12,num1,f1))

# \\   特殊字符转换成正常字符
print("hello \n world!")
print("hello \\n world!")

# \'  \"     实现tom is 'good' man
print('tom is \'good\' man')
print('tom is \"good\" man')

#如果字符串内有很多换行,用\n写在一行不好阅读
print("tom\nis\ngood\nman")

print('''
tom 
is 
good
man
''')

# \t 制表符
print("tom\tgood")

#只想打印 \\\t\\
#如果字符串中有很多字符串需要转义,就需要加入好多\,为了简化,Python允许用r表示内部的字符串默认不转义
print(r"\\\t\\")
#打印windows路径
print(r"E:\test\test\users")


#字符串方法
#eval(str)
#功能：将字符串的str当成有效的表达式来求值并返回计算结果
num1 = eval("123")
print(num1)
print(type(num1))
print(eval("123"))
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12%3"))
#print(eval("a123"))

#len(str)
#功能：返回字符串的长度(字符个数)
print(len("hello,world"))

#lower()
#功能：转换字符串中大写字母为小写字母
str14 = "HELLO,world!"
print(str14.lower())

#upper()
#功能：转换字符中小写字母为大写字母
str15 = "HELLO,world!"
print(str15.upper())

#swapcase()
#功能：转换字符串中小写字母为大写字母,大写字母为小写字母
str16 = "HELLO,world!"
print(str16.swapcase())

#capitalize()
#功能：首字母大写，其他小写
str17 = "HELLO,world!"
print(str17.capitalize())

#title()
#功能：每个单词的首字母大写
str18 = "HELLO,world!"
print(str18.title())

#center(width[,fillchar])
#功能：返回一个指定宽度的居中字符串,fillchar为填充的字符串，默认是空格填充
str20 = "HELLO,world!"
print(str20.center(40,"*"))

#ljust(width[,fillchar])
#返回一个指定宽度的左对齐字符串,fillchar为填充字符,默认空格填充
str21 = "HELLO,world!"
print(str21.ljust(40,"%"))

#rjust(width[,fillchar])
#返回一个指定宽度的右对齐字符串,fillchar为填充字符,默认空格填充
str22 = "HELLO,world!"
print(str22.rjust(40,"%"))

#zfill(width)
#返回一个长度为width的字符串,原字符串右对齐,前面补0
str23 = "hello,world!"
print(str23.zfill(40))

#count(str[,start][,end])
#返回字符串中str出现的次数,可以指定一个范围,默认从头到尾
str24 = "tom is a very very nice man"
print(str24.count("very",10,len(str24)))

#find(str[,start][,end])
#从左向右检测str字符串是否包含在字符串中,可以指定范围,默认从头到尾.得到的是第一次出现的开始下标,没有返回-1
str25 = "tom is a very very nice man"
print(str25.find("very"))
print(str25.find("good"))
print(str25.find("very",10,len(str25)))

#rfind(str[,start][,end])
#从右向左检测str字符串是否包含在字符串中,可以指定范围,得到的是第一次出现的开始下标,没有返回-1
str26 = "tom is a very very nice man"
print(str26.rfind("very"))
print(str26.rfind("good"))
print(str26.rfind("very",10,len(str26)))

#index(str,start=0,end=len(str))
#跟find()功能一样,只不过如果str不存在的时候会报一个异常
str27 = "tom is a very very nice man"
#print(str27.index("good"))

#rindex(str,start=0,end=len(str))
#跟rfind()功能一样,只不过如果str不存在的时候会报一个异常
str28 = "tom is a very very nice man"
#print(str28.index("good"))

#lstrip()
#截掉字符串左侧指定的字符,默认为空格
str29 = "    tom is a very very nice man"
str30 = "********tom is a very very nice man"
print(str29.lstrip(),"\n",str30.lstrip("*"))

#rstrip()
#截掉字符串右侧指定的字符,默认为空格
str31 = "tom is a very very nice man    "
print(str31.rstrip(), "*")


#strip()
#截掉字符串两边指定的字符，默认为空格
str32 = "**********tom is a very very nice man**********"
print(str32.strip("*"))


#ord()
#字符串转换成ASCII值
str33 = "A"
print(ord(str33))

#chr()
str34 = 65
print(chr(str34))