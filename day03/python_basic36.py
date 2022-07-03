"""
# @Time : 2022/5/2 0002 15:53
# @File : python_basic36
# @Project : pythonWfd
# @Content :
"""

"""
各数据类型共同特征和不同特征
1、从保存方式来看，列表、元组、字典都可以保存一组数据
2、列表和元组是可以通过下标访问的，集合和字典没有下标，字典可以通过kry访问value
3、增删改方式不同
可变类型：列表，集合，字典       (值可以改变)
不可变类型：数字，字符串，元组    (值不能发生改变)   
"""
# 1、从保存方式来看，列表、元组、字典都可以保存一组数据
# 保存一组双色球
list1 = [1, 7, 11, 15, 19, 22, 6]
tuple1 = (1, 7, 11, 15, 19, 22, 6)
set1 = {1, 7, 11, 15, 19, 22, 6}
dict1 = {"第一个球": 1, "第二个球": 7, "第三个球": 11, "第四个球": 15, "第五个球": 19, "第六个球": 22, "第七个球": 6}

# 2、列表和元组是可以通过下标访问的，集合和字典没有下标，字典可以通过key访问value
print(list1[3])  # 15
print(tuple1[2])  # 11
# print(set1[4])  # 集合无法下标访问
print(dict1["第三个球"])  # 11 字典可以通过kry访问value    .get(key)

# 3、增删改方式不同
# (1)各类型的新增方式
# 列表
list1.append("a")  # 列表增加元素用 append()
print(list1)
# 元组
print("元组不可变类型，不能进行增删改")
# 集合
set1.add("a")  # 集合增加元素用add
print(set1)
# 字典
dict1["第八个球"] = 666  # 字典增加直接用self[key] = value 这个key是原字典不存在的
print(dict1)

# (2)各类型的删除方式
# 列表
list1.pop(1)  # 通过下标的方式删除 使用pop()
list1.remove(11)  # 列表删除对应的元素10 使用remove()
# 元组
print("元组不可变类型，不能进行增删改")
# 集合
set1.remove(15)  # 集合直接通过值进行删除
# 字典
dict1.pop("第八个球")  # 字典通过key删除

# (3)各数据类型，修改数据
# 列表
list1[0] = 777  # 列表可通过下标直接修改
print(list1)  # [777, 15, 19, 22, 6, 'a']
# 元组和集合
print("元组不可变类型，不能进行增删改")
print("集合没有下标，不可以直接修改值")
# 字典
dict1["第一个球"] = 777  # 直接通过key修改value
print(dict1)  # {'第一个球': 777, '第二个球': 7, '第三个球': 11, '第四个球': 15, '第五个球': 19, '第六个球': 22, '第七个球': 6}

# 4、列表、元组、字典、集合的其他公共的API
list1 = [1, 7, 11, 15, 19, 22, 6]
tuple1 = (1, 7, 11, 15, 19, 22, 6)
set1 = {1, 7, 11, 15, 19, 22, 6}
dict1 = {"第一个球": 1, "第二个球": 7, "第三个球": 11, "第四个球": 15, "第五个球": 19, "第六个球": 22, "第七个球": 6}

# (1)切片：有下标的数据类型(字符串、列表、元组)可以通过切片获取一部分值
str1 = "abcdefg"
print(str1[0:5])  # abcde 截取0号位置开始，在5号位置结束，前包含，后不包含
print(str1[1:4])  # bcd   截取1号位置开始，在4号位置结束，不包含4号位置
print(str1[-5:-2])  # cde
# 元组和列表进行切片
print(list1[1:6])  # [7, 11, 15, 19, 22]
print(tuple1[1:-2])  # (7, 11, 15, 19)
print(list1[:6])  # [1, 7, 11, 15, 19, 22]
print(list1[3:])  # [15, 19, 22, 6]

# (2)求长度 len()
print(len(list1), len(tuple1), len(set1), len(dict1))  # 7 7 7 7

# (3) 判断某个元素是否存在 列表、元组、集合、字典中 使用in\not in
print(7 in list1)  # True 7在list1里面，给出结果True
print(7 not in list1)  # False 表达式不成立 给False
print("第一个球" in dict1)  # True 字典是判断值是否存在于key里面
print(1 in dict1)  # False 这个表达式是判断1是否存在于dict1的key里面
# 如果需求判断1是否存在字典的value里面
print(1 in dict1.values())  # True 这个表达式判断1是否存在value里面，先通过 dict1.values()获取所有的value，在进行判断

# (4)求 列表、元组、集合、字典中：最大值(max) / 最小值(min) /求和sum()
print("列表list1最大值为：{}，最小值为：{}，和为：{}".format(max(list1), min(list1), sum(list1)))
print("元组tuple1最大值为：{}，最小值为：{}，和为：{}".format(max(tuple1), min(tuple1), sum(tuple1)))
print("集合set1最大值为：{}，最小值为：{}，和为：{}".format(max(set1), min(set1), sum(set1)))
# 要求字典的最大值、最小值、和需要先将字典的value拿出来
values = dict1.values()
print(values)  # dict_values([1, 7, 11, 15, 19, 22, 6])
print("字典dict的最大值为：{}，最小值为：{}，和为：{}".format(max(values), min(values), sum(values)))

# (5)字符串、列表、元组中，统计元素出现的次数用count()
str1 = "i am a teacher"
print(str1.count("a"))  # 3  a在字符串str1中出现的次数

list2 = ["a", "b", "a", "d", "b", "c", "d"]
print(list2.count("b"))  # 2

# (6)字符串、列表、元组 可以相互合并 使用+
# 字符串
str1, str2, str3 = "i", "love", "you"
str4 = str1 + str2 + str3
print(str4)  # iloveyou
# 列表
lst1, lst2 = [1, 2, 3], [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)  # [1, 2, 3, 4, 5, 6]
# 元组
tup1, tup2 = (1, 2, 3), (4, 5, 6)
tup3 = tup1 + tup2
print(tup3)  # (1, 2, 3, 4, 5, 6)

# (7)列表、元组、字符串、集合的相互转换
# 列表转元组
lst = [1, 2, 3]
tup = tuple(lst)
print(tup, type(tup))  # (1, 2, 3) <class 'tuple'>

# 字符串转列表
str1 = '15821873878'
lst = list(str1)
print(lst)  # ['1', '5', '8', '2', '1', '8', '7', '3', '8', '7', '8']

# 字符串转集合，因为集合不能重复，所以相同元素会被过滤掉
str1 = '15821873878'
set_number = set(str1)
print(set_number)  # {'8', '7', '2', '1', '3', '5'}

# (8)del 删除，该函数可以删除任意数据
nike_name = "小花"
print(nike_name)
del nike_name
# print(nike_name)  # NameError: name 'nike_name' is not defined

list1 = [1, 2, 3, 54]
del list1[-1]
print(list1)  # [1, 2, 3]
