'''
break语句：
作用：跳出for和while循环
注意：只能跳出距离他最近的那一层循环
'''

for i in range(10):
    print(i)
    if i == 5:
        break

a = 1
while a <= 3:
    print("test1!")
    a += 1
    if a == 2:
        break
#注意：循环语句可以有else语句,break导致循环截止,不会执行else下面的语句
else:
    print("test2!")