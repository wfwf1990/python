# Author: wangfang
#队列：先进先出

import collections
#创建一个队列
queue = collections.deque()

#进队列：存数据
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)

#出队列：取数据
res1 = queue.popleft()
print("res1 = ", res1)
res2 = queue.popleft()
print("res2 = ", res2)
res3 = queue.popleft()
print("res3 = ", res3)