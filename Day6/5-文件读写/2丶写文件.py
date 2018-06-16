# Author: wangfang

#方式二：
#将信息写入到缓冲区
path = r"C:\Users\lovebaby\PycharmProjects\python\Day6\5-文件读写\file1"
f = open(path,"w+")
f.write("tom is good man\n")
#刷新缓冲区:直接把内部缓冲区的数据立刻写入文件,而不是被动的等待自动刷新缓冲区写入
f.flush()
f.close()

#方式二：
with open(path,"a") as f2:
    f2.write("good man!\n")
