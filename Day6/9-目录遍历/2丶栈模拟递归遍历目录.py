# Author: wangfang
import os
def getAllDir(path):
    #创建一个空栈
    stack = []
    #压栈
    stack.append(path)
    #处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        #从栈里取出数据
        dirpath = stack.pop()
        #列出目录下的所有文件
        filelist = os.listdir(dirpath)
        #处理每一个文件，如果是普通文件则打印出来,如果是目录则将目录的地址压栈
        for filename in filelist:
            absfile = os.path.join(dirpath, filename)
            if os.path.isdir(absfile):
                print("目录 = " , absfile)
                stack.append(absfile)   #目录压栈
            else:
                print("普通文件 = ", absfile)




path = r"F:\python\pack4\python\千锋Python基础全套视频教程\千锋python基础教程：第一章 python语言基础"
getAllDir(path)