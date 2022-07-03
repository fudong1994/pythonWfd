"""
============================
   Author: Lee
   date  : 2022/5/22 - 14:46
=============================
"""

"""
面试问题:
1.什么是栈、堆
2.小整数池和大整数池的作用
3.is 和 == 区别
"""

a = 100
b = 100
print('a的地址是:', id(a))  # a的地址是: 140722836070528
print('b的地址是:', id(b))  # b的地址是: 140722836070528

a = 9999999999999
b = 9999999999999
print('a的地址是:', id(a))  # a的地址是: 1824798347856
print('b的地址是:', id(b))  # b的地址是: 1824798347856

# 身份运算符 is (判断两个标识符是否同一对象,直接比对物理地址)
# is not (判断两个标识符是否不是同一对象,直接比对物理地址)
a = 100
b = 100
print(id(a), '************', id(b))  # 140722828140672 ************ 140722828140672
print(a is b)  # True

b = 30
print(id(a), '************', id(b))  # 140722828140672 ************ 140722828138432
print(a is b)  # False
