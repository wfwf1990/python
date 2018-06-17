# Author: wangfang
#栈特点：先进后出

#模拟栈结构
stack = []

#压栈（向栈里存数据）
stack.append("A")
stack.append("B")
stack.append("C")
print(stack)

#出栈（在栈里取数据）
res1 = stack.pop()
print(res1)
print(stack)
res2 = stack.pop()
print(res2)
print(stack)
res3 = stack.pop()
print(res3)
print(stack)