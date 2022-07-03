"""
# @Time : 2022/5/8 0008 10:03
# @File : python_basic41
# @Project : pythonWfd
# @Content :条件判断
"""

"""
本章讲解：条件判断
"""

"""
条件判断分为单分支语句、双分支和多分支语句

单分支语句语法：
if 条件：
    语句块

"""
# 单分支
if True:
    print("你真棒")

"""
双分支语句语法：
if 条件：
    语句块1
else:
    语句块2
"""
# 双分支案例1：用户从控制台输入整数，判断是奇数还是偶数
num = int(input("请输入一个整数："))
if num % 2 == 0:
    print("{}是偶数".format(num))
else:
    print("{}是奇数".format(num))

# 用户输入一个年份，判断是否为闰年(能被4整除并且不能被100整除，或者能被400整除)
year = int(input("请输入年份："))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("{}是闰年".format(year))
else:
    print("{}不是闰年".format(year))