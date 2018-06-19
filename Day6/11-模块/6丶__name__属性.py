'''
__name__属性：
    模块就是一个可执行的.py文件,一个模块被另一个程序引入;我不想让模块中的某些代码执行,
    可以用__name__属性来使程序仅调用模块中的一部分
'''

#每一个模块都有一个__name__属性,当其值等于"__main__"时,表示该模块自身在执行
#当前文件如果为程序的入口文件，则__name__属性的值为__main__
if __name__ == "__main__":
    print("这是tom.py文件")
    print(__name__)
else:
    def sayGood():
        print("tom is good man!")
    def sayNice():
        print("tom is nice man!")
    def sayGreat():
        print("tom is great man!")


