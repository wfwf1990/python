# Author: wangfang
import re

'''
匹配单个字符与数字
    .               匹配除换行符以外的任意单个字符
    [0123456789]    []是字符集合,表示匹配方括号中所包含的任意一个字符
    [god]            匹配'g' 'o' 'd' 中任意一个字符
    [a-z]            匹配任意小写字母
    [A-Z]           匹配任意大写字母
    [0-9]           匹配任意单个数字,类似[0123456789]
    [0-9a-zA-Z]     匹配任意的数字和字母包含大小写
    [0-9a-zA-Z_]     匹配任意的数字和字母包含大小写和下划线
    [^god]          匹配除了'g' 'o' 'd'这几个字母以外的所有字符，中括号例的^称为脱字符,表示不匹配集合中的字符
    [^0-9]          匹配所有的非数字字符
    \d              匹配数字,效果通[0-9]
    \D              匹配非数字字符,效果同[^0-9]
    \w              匹配数字，字母和下划线,效果同[0-9A-Za-z_]
    \W              匹配非数字,字母和下划线，效果同[^0-9a-zA-Z]
    \s              匹配任意的空白符(空格,换行,回车，换页，制表)，效果等同于[ \f\n\r\t]
    \S              匹配任意的非空白字符，效果同[^ \f\n\r\t]
'''
print(re.findall(".","tom is good man!"))
print(re.findall(".","tom is \ngood man!",flags=re.S))   #把\n当做一个字符
print(re.findall("[0-9]","tom is good man! 6"))
print(re.findall("[\d]","tom is good man! 6"))
print(re.findall("[good]","tom is good man! 6"))


'''
匹配边界字符
    ^       行首匹配，和在[]里的^不是同一个意思
    $       行尾匹配
    \A      匹配字符串开始，它和^的区别是，\A只匹配整个字符串的开头,即使在re.M模式下也不会匹配它行的行首
    \Z      匹配字符串结束,它和$的区别是,\Z只匹配整个字符串的结束,即使在re.M模式下也不会匹配它行的行尾
    
    \b      匹配一个单词的边界，也就是指单词和空格间的位置,扩展元字符
    \B      匹配非单词边界
'''
print(re.findall("^tom","tom is good man"))
print(re.findall("man$","tom is good man"))

print(re.findall("^tom","tom is good man\ntom is good man",flags=re.M))  #^每一行都会匹配
print(re.findall("\Atom","tom is good man\ntom is good man",flags=re.M))  #\A 只会匹配一行

print(re.findall("man$","tom is good man\ntom is good man",flags=re.M))  #^每一行都会匹配
print(re.findall("man\Z","tom is good man\ntom is good man",flags=re.M))  #\A 只会匹配一行

print(re.findall(r"\ber\b","er"))   #匹配整个单词
print(re.findall(r"\btom\b","123tom123"))


'''
匹配多个字符:下方的x丶y丶z均为假设的普通字符,不是正则表达式的字符
    (xyz)       匹配小括号内的xyz（作为一个整体去匹配）
    x？          匹配0个或者1个x
    x*          匹配0个或者任意多个x
    .*          表示匹配0个或者任意多个字符，匹配整行
    x+          匹配至少一个x
    x{n}        匹配确定的n个x（n是一个非负整数）
    x{n,}       匹配至少n个x
    x{n,m}      匹配至少n个x，最多m个x，注意n<=m
'''

print(re.findall(r"(tom)","tom is good man")) #非贪婪匹配（尽可能少的匹配）
print(re.findall(r"a?","aaabaa"))       #贪婪匹配（尽可能多的匹配）print(re.findall(r"a*","aaabaa"))
print(re.findall(r"a+","aaabaa"))   #贪婪匹配（尽可能多的匹配）
print(re.findall(r"a{3}","aaabaa"))


'''
特殊：
    *?  +? x? 最小匹配，通常都是尽可能多的匹配，可以使用这种解贪婪匹配解决
    (?:x)   类似(xyz)，但不表示一个组
'''

str1 = "tom is good man,tom is good man"
print(re.findall("tom.*?man",str1))
print(re.findall("(?:tom)",str1))\



