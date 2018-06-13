'''
def fun1(name):
    print("%s is a good man" %(name))
def outer(func):
    def inner(name):
        print("*********")
        func(name)
    return inner

f = outer(fun1)
f("tom")
'''





#使用@符号将装饰器应用到函数
def outer(func):
    def inner(name):
        print("*********")
        func(name)
    return inner

@outer   #相当于fun1 = outer(fun1)
def fun1(name):
    print("%s is a good man" %(name))
fun1("tom")