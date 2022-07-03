"""
# @Time : 2022/5/29 0029   10:15
# @File : python_basic71
# @Project : pythonWfd
# @Content :组包、拆包
"""

"""
组包/装包：通俗的讲，组包就是把多个数据装在一个元组中
拆包/解包：把一组数据进行拆分，比如 列表/字典/元组等拆分成单个数据
"""

# 自动组包 任意无符号对象以逗号隔开，会自动组包成一个元组
a = 1, 2, 3, 4
print(a)  # (1, 2, 3, 4) 将多个元素组装成一个元组

b = '老刘', '老徐', '心凌男孩'
print(b)

# 自动拆包 变量的个数要与被拆包对象中的元素个数一致
b1, b2, b3 = b
print(b1)
print(b2)
print(b3)

# 手动拆包 *
print(*b)
a1, *a2 = b
print(a1)
print(a2)

*c1, c2 = b
print(c1)
print(c2)

# 对字典的操作，默认是操作键
dict1 = {'心凌男孩': '25', '性别': '男', '户籍': '安徽'}
d1, d2, d3 = dict1
print(d1)
print(d2)
print(d3)
