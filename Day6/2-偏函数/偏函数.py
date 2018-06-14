

#二进制转换成十进制
print(int("1010",base = 2))


#偏函数
def int2(str,base = 2):
    return int(str,base)
print(int2("1010"))


import functools
int3 = functools.partial(int,base = 2)
print(int3("1010"))