'''
字典：
    使用键-值（key-value）存储,具有极快的查找速度
key的特性：
    1丶字典中的key必须唯一
    2丶key必须是不可变的对象
    3丶字符串丶整数等都是不可变,可以作为key
    4丶list是可变的,不能作为key

'''
#1）创建字典
dict1 = {"tom":60,"jack":70}

#（2）元素的访问
#1）获取：字典名[key]
dict2 = {"tom":60,"jack":70}
print(dict2["tom"])

print(dict2.get("tom1")) #key不存在,返回none

ret = dict2.get("tom1")
if ret == None:
    print("没有!")

#（3）添加
#一个key对应一个value,所以多次对一个key的value赋值,其实就是修改值
dict3 = {"tom":60,"jack":70}
dict3["wf"] = 80
print(dict3)

#（4）删除
#根据key删除
dict4 = {"tom":60,"jack":70}
dict4.pop("tom")
print(dict4)

#（5）字典遍历
#1）方式一：
dict5 = {"tom":60,"jack":70}
for i in dict5:
    print(i,dict5[i])

#2）遍历value
dict6 = {"tom":60,"jack":70}
print(dict6.values())   #[60, 70]
for i in dict6.values():
    print(i)
#3）
dict7 = {"tom":60,"jack":70}
print(dict7.items())        #[('jack', 70), ('tom', 60)]
for k,v in dict7.items():
    print(k,v)

#4）
dict8= {"tom":60,"jack":70}
for k,v in enumerate(dict8):
    print(k,v)