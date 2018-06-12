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

print(dict2.get("tom"))
