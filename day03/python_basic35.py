"""
# @Time : 2022/5/2 0002 15:21
# @File : python_basic35
# @Project : pythonWfd
# @Content :字典
"""

"""
字典：以key(键)-value(值)形式来保存数据 {key1:value1,key2:value2,key3:value3.....}

"""
# 1、字典的定义
dict1 = {}  # 定义一个空字典
dict2 = {'name': 'xiaohua', 'age': 18, 'sex': '女'}

# 2、使用key获取value
print("name键对应的值为", dict2['name'])  # name键对应的值为 xiaohua

# 3.通过key获取value 方式2：.get()
print("name键对应的值为", dict2.get('name'))  # name键对应的值为 xiaohua

# 4、通过key修改value
dict2["name"] = "xiaohuahua"
print(dict2)  # {'name': 'xiaohuahua', 'age': 18, 'sex': '女'}

# 5、根据key删除value，删除性别
dict2.pop("sex")
print("删除后的字典", dict2)  # {'name': 'xiaohuahua', 'age': 18}

# 6、添加一个键值对 key存在的话，进行修改，key不存在，进行新增
dict2["tel"] = "15821873878"
print("添加tel键值对后的字典", dict2)  # {'name': 'xiaohuahua', 'age': 18, 'tel': '15821873878'}

# 7、其他知识
dict3 = {'name': 'xiaohua', 'age': 18, 'sex': '女', 'tel': '15821873878'}
# 获取所有的key，使用.keys()
ks = dict3.keys()
print(ks)  # dict_keys(['name', 'age', 'sex', 'tel'])

# 获取所有的value，使用.values
va = dict3.values()
print(va)  # dict_values(['xiaohua', 18, '女', '15821873878'])

# 获取所有的键值对，使用items()
kvs = dict3.items()
print(kvs)  # dict_items([('name', 'xiaohua'), ('age', 18), ('sex', '女'), ('tel', '15821873878')])

# key不能重复，如果一个字典声明的时候有重复的key，后面的值会覆盖前面的值
dict3 = {'name': 'xiaohua', 'age': 18, 'sex': '女', 'tel': '15821873878', 'name': 'xiaobai'}
print(dict3)  # {'name': 'xiaobai', 'age': 18, 'sex': '女', 'tel': '15821873878'}
