
'''
#计算字符串数字的和
str1 = input("input:")
index = 0
sum = 0
while index < len(str1):
    if str1[index] >= "0" and str1[index]<= "9":
        sum += int(str1[index])
    index += 1
print("sum = %d" %(sum))
'''



#字符串比较大小,结果返回True或False
#从第一个字符开始比较，谁的ASCII值大谁就大,如果相等会比较下一个字符的ASCII的大小,那么谁的值大谁就大
print("ab" > "az")
print(ord("b"),ord("z"))

#输入5个数字,找出第二大的值
'''
list = []
for i in range(5):
    num = int(input("input:"))
    list.append(num)
print(list)

list.sort()
index = 0
#list[len(list)-1]
#list.count(list[len(list)-1])
count = list.count(list[len(list)-1])
while index < count:
    list.pop()
    index += 1
print(list[len(list)-1])
'''

#输入字符串,计算有多少个单词
# deadsad dsadas dsad

str = input("input:")
str1 = str.strip()
index = 0
count = 0
while index < len(str1):
    while str1[index] != " ":
        index += 1
        if index == len(str1):
            break
    count += 1
    if index == len(str1):
        break
    while str1[index] == " ":
        index += 1
print("count is %d"  %(count))