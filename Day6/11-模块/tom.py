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