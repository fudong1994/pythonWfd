"""
# @Time : 2022/5/15 0015   15:38
# @File : python_basic53
# @Project : pythonWfd
# @Content :
"""


"""
循环嵌套
"""

print(1)  # 打印()中的内容，并且换行
print(2, end=' ')  # 打印()中的内容，并且不换行
print(3)

# 打印一个4行5列的矩形
#  *****
#  *****
#  *****
#  *****

for j in range(4):
    print('*****')

print('===' * 50)

# 打印单行
for j in range(5):
    print('*', end='')

print()
print('===' * 50)

# 外循环循环一次，内循环必须全部循环完成
for i in range(4):  # 外循环  0,1,2,3
    for j in range(5):  # 内循环 01234  01234  01234  01234
        print('*', end='')
        # *****
        # *****
        # *****
        # *****

    print()  # 内循环全部完成一次，换一次行

# 打印一个直角三角形

# 一共4行，外循环循环4次，第一次循环打印 1个*    第二次循环打印2个*  第三次循环打印3个*  第四次循环打印4个*
# *
# **
# ***
# ****

for i in range(4):  # 外循环  0  1  2  3
    for j in range(i + 1):
        print('*', end='')  # *
        # **
        # ***
        # ****
    print()

for i in range(1, 5):  # 外循环  1,2,3,4
    for j in range(i):  # 第一次循环打印 1个*    第二次循环打印2个*  第三次循环打印3个*  第四次循环打印4个*
        print('*', end='')
    print()

print('===' * 50)

# 打印99乘法口诀表

for i in range(1, 10):  # i = 1,2,3,4,5,6,7,8,9
    for j in range(1, i + 1):  # j = 1,2,3,4
        print('{}*{}={}'.format(j, i, i * j), end=' ')
        # 1*1 = 1
        # 1*2 = 2  2*2 = 4
        # 1*3 = 3  2*3 = 6  3*3 = 9
        # 1*4 = 4  2*4 = 8  3*4 = 12  4*4 = 16
        #
    print()
