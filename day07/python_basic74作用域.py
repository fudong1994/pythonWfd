"""
# @Time : 2022/5/29 0029   15:52
# @File : python_basic74作用域
# @Project : pythonWfd
# @Content :
"""

"""
作用域：为了编写可维护代码，我们把很多代码，放在不同的区域中
模块：一个py文件称之为一个模块
"""

# 知识点1：变量的作用域：变量分为全局变量(定义在模块中,任何地方都能使用) 和局部变量(定义在函数中,只有该函数内有效)
a = 100  # 全局变量，定义在模块中


def fun1():
    b = 200  # b是局部变量 定义在函数中，只在该函数内有效
    print(a)  # a是全局变量，在整个模块中都能使用
    print(b)  # b可以打印，因为它属于fun1()


fun1()

# print(b) #该行代码报错，因为b属于fun1()，只在fun1()函数内有效


# 知识点2：global  可以在函数内使用全局变量，只有该函数运行后，该变量才会起作用
c = 100


def fun2():
    global c
    c = 200
    print(c)


print('===' * 50)

print(c)  # 100
fun2()  # 200
print(c)  # 200


# 知识点3：函数嵌套
def fun3():
    a = 10

    def fun4():
        print('内部函数')

    fun4()  # 调用fun4()函数
    print(a)


print('===' * 50)
fun3()


# 知识点4： nonlocal  #用来修改外部嵌套函数的作用域的值，nonlocal只能写在嵌套函数中
def fun4():
    a = 10

    def fun5():
        nonlocal a  # 代表外层函数的变量a
        a = 20

    fun5()  # 调用fun5()函数
    print(a)  # 20


print('===' * 50)
fun4()
