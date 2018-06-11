'''
for循环语句：
格式：
for 变量名 in 集合:
    语句

逻辑：按顺序取"集合"中的每个元素赋值给"变量",在去执行语句,如此循环往复,直到取完"集合"中的元素为止
'''

for i in [1,2,3,4,5]:
    print(i)


'''
range([start,] end[,step])函数： 列表生成器
start默认为0,step默认为1
'''

for  x in range(5):    #生成0到5-1的数列
    print(x)
for y in range(2,20,2):
    print(y)

#同时获取下标和元素
for x,y in enumerate([1,2,3,4,5]):
    print(x,y)

#求1到100的和
sum = 0
for i in range(1,101):
    sum += i
print(sum)