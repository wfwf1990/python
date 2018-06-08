



#打印出所有三位数中的水鲜花数
num = 100
while num <= 999:
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
    if num == num1 ** 3 + num2 ** 3 + num3 ** 3:
        print(num)
    num += 1


ge = " "
str1 = input("str:")
print(str1.count(" "))

