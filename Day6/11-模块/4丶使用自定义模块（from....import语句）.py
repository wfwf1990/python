#只想使用模块中一部分的函数功能
'''
from.....import 语句
 作用：从模块中导入一个指定的部分函数功能到当前的命名空间
格式：from module import name1[,name2][,namen]
'''
#导入tom模块中的sayGood函数功能
from tom import sayGood,sayGreat
'''
程序内容的函数可以将模块中的同名函数覆盖
def sayGood():
    print("tom")
'''


sayGood()
sayGreat()
#sayNice()  #没有引入sayNice模块