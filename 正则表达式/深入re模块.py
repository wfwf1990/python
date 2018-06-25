# Author: wangfang
import re
#re.split 字符串切割
str2 = "tom    is  good man"
print(str2.split(" "))
print(re.split("\W+",str2))         #除了字母数字以外的字符切割，这里以空格字符切割


#re.finditer 和 findall类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
str3 = "12a32bc43jf3"
print(re.findall("\d+",str3))
it1 = re.finditer("\d+",str3)
for match in it1:
    print(match.group())

#re.sub  字符串的替换和修改
'''
语法：re.sub(pattern, repl, string, count=0)
参数：
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''

phone = "2004-959-559 # 这是一个电话号码"

#删除注释
num = re.sub("#.*$","",phone)
print("num = %s" %num)

#删除非数字字符
num = re.sub("\D+","",phone)
print(num)







'''
分组：除了简单的判断是否匹配之外,正则表达式还有提取子串的功能,用()表示的就是提取分组

'''

str4 = "2004-959-559"
m = re.match("(\d{4})-(\d{3})",str4)
print(m.group(0))     #使用序号获取对应组的信息，group(0)一直代表的是原始字符串
print(m.group(1))
print(m.group(2))

print(m.groups())       #查看各组情况


#compile 函数

'''
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
re.compile(pattern[, flags])
'''

pattern = re.compile(r"\d+")   #编译成正则对象，用于匹配至少一个数字
str5 = "fda12312cdsas"
print(pattern.match(str5))   #查找头部，没有匹配
m = pattern.match(str5,3,5)  #从1的位置开始匹配，正好匹配，返回一个match对象
print(m)

print(pattern.findall(str5))
