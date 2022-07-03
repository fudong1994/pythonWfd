"""
# @Time : 2022/5/8 0008 14:23
# @File : python_basic43
# @Project : pythonWfd
# @Content : while循环
"""

"""
while循环：

语法：
while 条件：
    语句块

当条件成立时执行语句块
"""

# 循环案例1：打印1-100
i = 0
while i < 100:
    i += 1
    print(i)

# 循环案例2：打印0-100的偶数
i = 0
while i <= 100:
    print(i)  # 0,2,4,6,8,10....100
    i += 2

# 求出1-100的偶数的数量
i = 1
count = 0  # 用来累计数量
while i <= 100:
    if i % 2 == 0:
        count += 1
    i += 1
print('1-100的偶数的数量为%d个' % count)

# 求出1-100的偶数的和
i = 1  # 开关
sm = 0
while i <= 100:
    if i % 2 == 0:
        sm += i
    i += 1
print('1-100的偶数和为：%d' % sm)

# 求出1-10的阶乘
i = 1
sm = 1
while i <= 10:
    sm = sm * i
    i = i + 1
print('1-10的阶乘结果为：%d' % sm)