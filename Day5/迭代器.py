'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象
可以用isinstance() 去判断一个对象是否是可迭代对象

可以直接作用于for的数据类型一般分两种
1丶集合数据类型，如list丶tuple丶dict丶set丶string
2丶generator，包括生成器和带yield的generator function

'''
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance((x for x in range(10)), Iterable))


'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出一个StopIteration错误表示无法继续返回下一个值
可以被next()函数调用并不断返回下一个值的对象称为迭代器
可以用isinstance() 去判断一个对象是否是可迭代对象
'''
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("",Iterator))
print(isinstance((x for x in range(10)), Iterator))    #迭代器


l = (x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#print(next(l))


#列表转换成迭代器
a = iter([1,2,3,4,5])
print(next(a))


print(isinstance(iter([]),Iterator))
print(isinstance(iter(()),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter(""),Iterator))

