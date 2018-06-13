


def outer(func):
    def inner(*args,**kwargs):
        #添加修饰的功能
        print("*******")
        func(*args,**kwargs)
    return inner

@outer
def fun1(name,age):
    print("my name is %s,i am  %d" %(name,age))


fun1("tom",18)