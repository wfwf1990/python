# Author: wangfang



def getAlldir(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dir1 = stack.pop()
        for dir2 in os.listdir(dir1):
            absfilename = os.path.join(dir1,dir2)
            if os.path.isdir(absfilename):
                stack.append(absfilename)
            else:
                fun1()


path = r"C:\Users\lovebaby\PycharmProjects\python\Day6\9-目录遍历"
getAlldir(path)