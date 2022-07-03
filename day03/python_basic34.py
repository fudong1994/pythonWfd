"""
# @Time : 2022/5/2 0002 14:36
# @File : python_basic34
# @Project : pythonWfd
# @Content :
"""

"""
可变类型：列表，集合，字典
不可变类型：数字，字符串，元组

有序：字符串，列表，元组
无序：数字，集合、字典
"""

# 查看物理地址 id()，地址随机分配的，每次运行都不一样


# 可变类型，可直接修改内容，比如列表
list1 = ['xiaohua ', 'xiaobai', 'xiaowang']
print(id(list1))  # 4153928 这个是更改前的物理地址
list1[1] = 'xiaohei'
print(list1)
print(id(list1))  # 4153928 这个是更改后的物理地址，与更改前一致，说明都是同一对象

# 区别一下重复赋值跟修改
a = 100
a = 200  # 重新赋值

b = [1, 2, 3]
b[1] = 222  # 这是修改内容

tup1 = ('xiaohua ', 'xiaobai', 'xiaowang')
print(id(tup1))
tup1 = ('xiaohua ', 'xiaohei', 'xiaowang')  # 重新赋值
print(id(tup1))

# 不可变类型，声明后不可修改内容，比如元组
tup1 = ('xiaohua ', 'xiaobai', 'xiaowang')
# tup1[1] = 'xiaohei' # 无法修改


# 有序：字符串，列表，元组，有下标，可以通过下标访问
stra = "abcdefg"
print(stra[0])  # a 可通过下标访问
lista = ['a', 'b', 'c']
print(lista[0])  # a 可通过下标访问
tupa = ('a', 'b', 'c')
print(tupa[0])  # a 可通过下标访问

# 无序：数字，集合、字典
inta = 12345
# print(inta[0]) # TypeError: 'int' object is not subscriptable
stea = {'a', 'b', 'c'}
# print(stea[0])  # TypeError: 'set' object does not support indexing
