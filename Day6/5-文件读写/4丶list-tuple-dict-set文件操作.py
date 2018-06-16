# Author: wangfang
import pickle
#1丶写
mylist = [1,2,3,4,5,"tom",{1:"good"}]
path = r"C:\Users\lovebaby\PycharmProjects\python\Day6\5-文件读写\file4"
f = open(path,"wb")         #打开文件
pickle.dump(mylist,f)       #写
f.close()                   #关闭

#2丶读
f1 = open(path,"rb")
templist = pickle.load(f1)
print(templist)
f.close()
