# Author: wangfang
'''

'''
'''
1丶获取传入函数的参数的path目录下的所有文件
'''
import os
def getAllDir(path,space = ""):
    dir1 = os.listdir(path)
    space = space + "   "
    #处理每一个文件
    for filelist in dir1:
        #获取文件的绝对路径
        absfile = os.path.join(path,filelist)
        #判断文件是目录还是文件
        if os.path.isdir(absfile):
            print(space + "目录 = " + filelist)
            getAllDir(absfile,space)  #还是目录继续递归,传入绝对路径
        else:
            print(space + "文件 = " + filelist)
            #pass

path = r"F:\python\pack4\python\千锋Python基础全套视频教程\千锋python基础教程：第一章 python语言基础"
getAllDir(path,"")
