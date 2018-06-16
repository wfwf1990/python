# Author: wangfang
#注意：二进制方式写入到文件一定要编码和解码
path = r"C:\Users\lovebaby\PycharmProjects\python\Day6\5-文件读写\file2"
#编码：以utf-8方式编码写入内容到文件中
with open(path,"wb") as f1:
    str = "我是个帅哥"
    f1.write(str.encode("utf-8"))

#解码，以utf-8方式解码从文件读取内容
with open(path,"rb") as f2:
    data = f2.read()
    newdata = data.decode("utf-8")
    print(newdata)

path1 = r"C:\Users\lovebaby\PycharmProjects\python\Day6\5-文件读写\file3"
with open(path1,"w",encoding="utf-8") as f3:
    f3.write("tom is 帅哥")
with open(path1,"r",encoding="utf-8") as f4:
    data1 = f4.read()
    print(data1)