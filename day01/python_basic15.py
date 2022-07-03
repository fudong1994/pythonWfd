'''
input函数：用来接受用户从控制台输入的类容
'''

# name = input("请输入姓名：")
# print(name)
# age = input("请输入年龄：")
# print(age)

# 设计一个两位数加法计算器，用户输入两位数字，打印出 两位数字 的和

# a = input("请输入第一个数字：")
# b = input("请输入第二个数字：")
# print(int(a) + int(b))

# 作业：解决 浮点型数据 进行数学运算，精度问题

print(round(11.22 + 33.55, 2))

import decimal
a = input("输入第一个数字:")
b = input("输入第二个数字:")
print(decimal.Decimal(a) + decimal.Decimal(b))



