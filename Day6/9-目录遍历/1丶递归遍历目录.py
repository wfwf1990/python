# Author: wangfang

import os
path = r"F:\python\pack4\python\千锋Python基础全套视频教程\千锋python基础教程：第一章 python语言基础"
def getAllDir(path,space = ""):
    dir1 = os.listdir(path)
    space = space + "   "
    for filelist in dir1:
        absfile = os.path.join(path,filelist)
        if os.path.isdir(absfile):
            print(space + "目录 = " + filelist)
            getAllDir(absfile,space)
        else:
            print(space + "文件 = " + filelist)

getAllDir(path,"")
