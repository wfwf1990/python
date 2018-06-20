# Author: wangfang
import os
def fun1(path):
    respath = r"C:\Users\lovebaby\PycharmProjects\python\Day6\9-目录遍历"
    with open(path,"r",encoding="utf-8") as f1:
        while True:
            f2 = f1.readline()
            #print(f2)
            if len(f2) < 5:
                break
            emailStr = f2.split("---")[0]
            dirstr = f2.split(".")[0].split("@")[1]
            print(dirstr)
            absdirstr = os.path.join(respath,dirstr)
            #print(dirstr)
            if not os.path.exists(absdirstr):
                os.mkdir(absdirstr)
            filepath = os.path.join(absdirstr,dirstr + ".txt")
            with open(filepath,"a",encoding="utf-8") as f10:
                f10.write(emailStr + "\n")

path = r"C:\Users\lovebaby\PycharmProjects\python\Day6\9-目录遍历\file3"
fun1(path)