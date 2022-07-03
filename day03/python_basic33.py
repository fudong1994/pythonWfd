"""
# @Time : 2022/5/2 0002 14:13
# @File : python_basic33
# @Project : pythonWfd
# @Content :集合 set
"""

"""
本章讲解：集合 set
集合的定义：{value1,value2,value3.....}
集合的特征：无序、没有索引、不能重复
注意：集合只能存放不可变类型的元素
"""

# 1、定义一个集合
set1 = set()  # 定义一个空集合
print(type(set1))  # <class 'set'>
set2 = {1, 7, 12, 14, 15, 21}
print(set2)

# 特征1：集合是无序的，打印出来的数据是乱序的，没有下标
set3 = {'aaa', 'bbb', 1, 2, 'ccc'}
print(set3)

# 特征2：没有下标索引，不能通过下标访问
set4 = {'aaa', 'bbb', 1, 2, 'ccc'}
# print(set4[0]) TypeError: 'set' object does not support indexing

# 特征3：集合的数据不能重复
set5 = {'aaa', 'bbb', 1, 2, 'ccc', 'aaa'}
print(set5)  # {1, 2, 'bbb', 'aaa', 'ccc'}自动进行去重

# 特征4：集合不能存放可变类型
# set6 = {'aaa', 'bbb', 1, 2, 'ccc', [1, 2, 3]} TypeError: unhashable type: 'list'
set6 = {'aaa', 'bbb', 1, 2, 'ccc', (1, 2, 3)}  # 元组属于不可变类型，可以放在集合中
print(set6)

# 2、集合删除元素用remove()，删除集合中的'aaa'
set7 = {'aaa', 'bbb', 1, 2, 'ccc'}
set7.remove('aaa')
print('删除元素"aaa"后', set7)

# 3、集合添加元素用add()  给set7添加元素'python'
set7.add('python')
print(set7)
