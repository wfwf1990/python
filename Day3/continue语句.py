'''
continue语句
作用：跳过当前循环中的剩余语句,然后继续下一次循环
注意：跳出最近的循环
'''

for i in range(10):
    print(i)
    if i == 3:
        continue

num = 0
while num < 10:
    if num == 3:
        num += 1
        continue
    print(num)
    num += 1