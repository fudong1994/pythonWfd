"""
知道点1：变量
"""
# #号为单行注释
# Ctrl+Alt+l 会自动调整格式

a = 100  # 声明一个变量a，并把值10赋值给a
print(a)
print(type(a))  # type() 用来查看变量的类型 <class 'int'> int代表整数类型
b = 10.5
print(b)  # 打印b的类容
print(type(b))  # <class 'float'> float代表浮点型

name1 = '小花'
print(type(name1))  # <class 'str'> str 代表字符串
name2 = "小花"
print(type(name2))  # <class 'str'> str 代表字符串
name3 = '''小花'''
print(type(name3))  # <class 'str'> str 代表字符串
name4 = """小花"""
print(type(name4))  # <class 'str'> str 代表字符串

# 变量值的覆盖
a = 10
print(a)  # 10
a = 20
print(a)  # 20
a = a + 20
print(a)  # 40

# 同时给多个变量赋值
a = b = c = 0
print(a, b, c)  # 打印a,b,c的值：0 0 0
A, B, C, D = 10, 20, 30, '小花'
print(A, B, C, D)  # 10 20 30 小花
