import time
time.clock()

def sum1(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

res = sum1(10000000)
print(time.clock())
print(res)

