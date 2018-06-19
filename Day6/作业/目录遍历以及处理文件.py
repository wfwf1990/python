
import os
#处理文件
def file(absfile):
    respath = r"D:\test1"
    with open(absfile,"r",encoding="utf-8") as f1:
        while True:
            f2 = f1.readline()
            print(f2)
            if len(f2) < 5:
                break
            mail = f2.split("----")[0]
            dir2 = f2.split("----")[0].split("@")[1].split(".")[0]
            abspath1 = os.path.join(respath,dir2)
            abspath2 = os.path.join(abspath1,dir2)
            if not os.path.exists(abspath1):
                os.mkdir(abspath1)
            with open(abspath2 + ".log","a",encoding="utf-8") as f2:
                f2.write(mail + "\n")
#遍历目录
def getAllFile(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dir1 = stack.pop()
        dir2 = os.listdir(dir1)
        for filelist in dir2:
            absfile = os.path.join(dir1,filelist)
            if os.path.isdir(absfile):
                print("目录 = ",absfile)
                stack.append(absfile)
            else:
                print("文件 = ",absfile)
                file(absfile)
path = r"D:\test"
getAllFile(path)