#一个.py文件就是一个模块

#引入模块
'''
import 语句：
    格式：import module1[,module2][,modulen]

'''
#引入自定义模块,不用加.py后缀
#注意：一个模块只会被引入一次，不管你执行了多少次import。防止模块被多次引入
import tom

#使用模块中的内容
#格式：模块名.函数名/变量名

tom.sayGood()
print(tom.num1)