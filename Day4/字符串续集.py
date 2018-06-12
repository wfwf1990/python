#split(str="")
#以str为分隔符截取字符串
str38 = "tom**is**good**man"
print(str38.split("*"))

#获取单词的个数,长度大于0就是一个单词
count = 0
for i in str38.split("*"):
    if len(i) > 0:
        count += 1
print(count)


#splitlines([keepends])  按照("\r","\r\n","\n")分隔,返回一个行数的列表
#keepends == True 会保留换行符
str39 = '''
tom is good man!
tom is nice man!
tom is price man!
'''
print(str39.splitlines())
print(str39.splitlines(True))


#join(seq)  以指定的字符串分隔符,将seq中的所有元素组合成一个字符串
list  = ['tom', '', 'is', '', 'good', '', 'man']
str40 = " ".join(list)
str41 = "&&".join(list)
print(str40)
print(str41)

#max() min()   获取字符串最大的字符
str42 = "tom is good man!z"
print(max(str42))

#replace(oldstr,newstr,count)
#用newstr替换oldstr,默认是全部替换,如果指定count数量,那么只替换前count个
str43 = "tom is good good man!"
str44 = str43.replace("good","nice")
print(str44)



#startswith(str,start=0,end=len(str))
#在给定的范围内判断是否以给定的字符串开头,如果没有指定范围,默认整个字符串
str45 = "tom is good man! "
print(str45.startswith("tom"))

#endswith(str,start=0,end=len(str))
#在给定的范围内判断是否以给定的字符串结尾,如果没有指定范围,默认整个字符串
str46 = "tom is good man"
print(str46.endswith("man"))


#encode(encoding="utf-8",error="ignore")
#编码
str47 = "tom is good man"
data47 = str47.encode("utf-8")
print(data47)

#decode
#解码
#注意：要与编码时的编码格式一致
str48 = data47.decode("utf-8")
print(str48)


#isalpha()
#如果字符串中至少有一个字符且所有的字符都是字母,例如不能有空格,返回True,否则返回False
str49 = "tom is good man"
print(str49.isalpha())

#isalnum()
#如果字符串中至少有一个字符且所有的字符都是字母或数字,返回True,否则返回False
str50 = "123ab"
print(str50.isalnum())

#isupper
#判断英文字符如果是大写返回True,否则返回False
str51 = "AB1"
print(str51.isupper())

#islower()
#如果字符串中至少有一个英文字符且所有的英文字符都是小写返回True,否则返回False

#istitle()
#如果字符串是标题话的返回True,否则返回False  ,单词的首字母是大写
print("Tom Is".istitle())

#isdigit()
#如果字符串中只包含数字字符返回True,否则返回False
print("123".isdigit())

#isnumeric() 同isdigit() 功能相同
print("1234".isnumeric())

#isspace()
#如果字符串中只包含空格则返回True,否则返回False \t \n \r也是空格
print(" ".isspace())
print("\t".isspace())
print("\n".isspace())




