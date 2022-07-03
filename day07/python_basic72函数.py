"""
# @Time : 2022/5/29 0029   11:03
# @File : python_basic72
# @Project : pythonWfd
# @Content :函数
"""

"""
函数：函数是可以重复使用的一段代码  比如：print()、id()、type()、input()....
函数的定义规则：
def 函数名([参数1,参数2,参数3....]):
    函数体(用来写具体的功能)
    [return] 代表结束该函数并且返回数据
"""


def add():
    print("我是一个自定义的函数add")


add()  # 根据函数名调用


def add1(a, b):
    c = a + b
    return c


# print(add1(1, 5))
d = add1(5, 8)
print(d)


# 设计一个函数，接收长方形的长、宽，返回面积
def area(length, wid):
    return length * wid


a1 = area(100, 30)
print(a1)


def add2(a, b):
    c = a + b
    c2 = a - b
    c3 = a * b
    return c, c2, c3  # 如果返回多个之，会自动把多个返回值打包成一个元组返回


print(add2(1, 6))
a2 = add2(1, 6)
print(a2, type(a2))  # (7, -5, 6) <class 'tuple'>


# 声明一个函数,判断是奇数还是偶数，并返回判断结果
def judge(num):
    if num % 2:
        return '%d是奇数' % num
    else:
        return '%d是偶数' % num


print(judge(3))