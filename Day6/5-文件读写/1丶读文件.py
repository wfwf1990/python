# Author: wangfang

'''
过程：
    1丶打开文件
    2丶读文件内容
    3丶关闭文件
'''

#（1）打开文件
'''
打开文件 ：open(path,flag[,encoding][,errors])
    path：要打开文件的路径
    flag：打开文件方式
flag打开文件方式：
    r  ：以只读的方式打开文件，文件的描述符放在文件的开头
    rb ：以二进制格式打开文件用于只读。文件描述符放在文件开头
    r+ ：打开一个文件用于读写,文件描述符放在文件开头
    w  ：打开一个文件，只用于写入，如果该文件已经存在会覆盖,不存在则创建一个新文件
    wb ：打开一个文件用于写入二进制,
    w+ ：打开一个文件用于读写
    a  ：打开一个文件用于追加，如果文件存在，文件描述符将会被放到文件末尾
    a+ ：
encoding：编码方式
    utf-8 
errors：错误处理
'''

path = r"C:\Users\lovebaby\PycharmProjects\python\Day6\5-文件读写\read"
f = open(path,"r",encoding="utf-8",errors="ignore")



#（2）读文件内容
'''
常用：read()  readline()  readlines()
'''
#1丶读取文件的全部内容,适合小文件
#str1 = f.read()
#print(str1)

#2丶读取指定字符数,注意文件描述符
#str2 = f.read(10)
#print("****" + str2 + "****")
#str3 = f.read(10)
#print("****" + str3 + "****")

#3丶读取整行,包括"\n"字符
'''
str4 = f.readline()
print(str4)
str5 = f.readline()
print(str5)
'''


#4丶读取指定字符数
#str6 = f.readline(10)
#print(str6)

#5丶读取所有行并返回列表
'''
list = f.readlines()
print(list)
'''

#修改描述符位置
str5 = f.read()
print(str5)
print("********")
f.seek(0)           #修改文件描述符至开头
print(str5)


#一个完整的过程
try:
    f1 = open(path,"r",encoding="utf8")
    print(f1.read())
finally:
    if f1:
        f1.close()

#打开文件，读文件，with自动关闭文件
with open(path,"r",encoding="utf8") as f2:
    print(f2.read())