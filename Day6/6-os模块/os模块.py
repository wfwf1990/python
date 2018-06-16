# Author: wangfang
#os模块：包含了普通的操作系统功能
import os
#os.name 获取操作系统类型,nt-->windows posix-->linux,unix
print(os.name)

#os.uname() 打印操作系统详细信息
#注意：windows不支持
#print(os.uname())

#os.environ获取操作系统的所有环境变量
print(os.environ)


#os.environ.get 获取指定环境变量

#os.curdir 获取当前目录 .
print(os.curdir)

#os.getcwd() 获取当前工作目录,即当前python脚本所在的目录
print(os.getcwd())

#os.listdir() 以列表形式返回指定目录下的所有文件
print(os.listdir())

#os.mkdir 在当前目录下创建新目录
#os.mkdir("tom")
#os.mkdir(r"C:\Users\lovebaby\PycharmProjects\python\Day6\6-os模块\tom")

#os.rmdir 删除目录
#os.rmdir("tom1")

#os.stat 获取文件详细属性
#print(os.stat("tom"))

#os.rename("oldname","newname")文件重命名
#os.rename("tom","jack")

#os.remove 删除文件
#os.remove(r"C:\Users\lovebaby\PycharmProjects\python\Day6\5-文件读写\file4")

#os.system 执行shell命令
#os.system("notepad")


#有些方法存在os模块里，还有些是在os.path里
#os.path.abspath() 查看当前的绝对路径
print(os.path.abspath("."))

#os.path.join 路径拼接
#注意路径2开始不要有斜杠
p1 = r"C:\Users\lovebaby\PycharmProjects\python\Day6"
p2 = "tom"
print(os.path.join(p1,p2))

