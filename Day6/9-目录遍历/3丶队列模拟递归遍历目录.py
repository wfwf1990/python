# Author: wangfang
import collections
import os
def getAllDir(path):
    #创建队列
    queue = collections.deque()
    #进队
    queue.append(path)
    while len(queue) != 0:
        #取数据
        getdir = queue.popleft()
        #列出当前目录下的所有文件
        filelist = os.listdir(getdir)
        #判断文件是否是目录还是文件
        for filename in filelist:
            #取文件的绝对路径
            absfilelist = os.path.join(getdir,filename)
            if os.path.isdir(absfilelist):
                print("目录 = ",absfilelist)
                queue.append(absfilelist)
            else:
                print("普通文件 = ",absfilelist)

path = r"F:\python\pack4\python\千锋Python基础全套视频教程\千锋python基础教程：第一章 python语言基础"
getAllDir(path)