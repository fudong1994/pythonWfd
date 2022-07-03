"""
# @Time : 2022/4/23 0023 14:18
# @File : python_basic22
# @Project : pythonWfd
# @Content : 字符串
"""
# 字符串的声明
name1 = "小花"
name2 = '小花'
name3 = '''小花'''
name4 = """小花"""

str1 = '你很"厉害"！'
print(str1)  # 你很"厉害"！

# 字符串可以使用+号拼接，结果还是一个字符串
str5 = "今天" + "天气" + "很好"
print(str5, type(str5))  # 今天天气很好 <class 'str'>   #通过拼接四个字符串成为了一个新的字符串
# 应用
# a = input("请输入第一个数：")
# b = input("请输入第二个数：")
# c = int(a) + int(b)
# print(a + "+" + b + "=" + str(c))

# 字符串的索引，字符串对每个字符做了编号，从前往后从0开始，从后往前从-1开始

# 通过下标获取指定位置的值
str6 = "今天是我们隔离的第45天！"
print(str6[0])  # 获取字符串str6下标为0的值：今
print(str6[-1])  # ！
print(str6[4])  # 们

# 通过下标截取部分值：切片  语法：str[开始下标：结束下标]   注意：前包含，后不包含
print(str6[3:5])  # 我们
print(str6[1:10])  # 天是我们隔离的第4
print(str6[-4:-1])  # 45天
print(str6[-9:9])  # 们隔离的第
print(str6[:5])  # 今天是我们
print(str6[5:])  # 隔离的第45天！
print(str6[::2])  # 今是们离第5！
print(str6[1::2])  # 天我隔的4天
print(str6[::3])  # 今我离4！

# 字符串填充
# .format()，字符串可以使用{}占位，再使用 format填充
str7 = "{}学校前段时间来了{}只大花猫，最近生了两只小{}".format("学校", 1, "白猫")
print(str7)  # 学校学校前段时间来了1只大花猫，最近生了两只小白猫

# 如果字符串中有动态（不断发生变化的值），可以使用format
a = input("请输入第一个数：")
b = input("请输入第二个数：")
c = int(a) + int(b)
# print(a + "+" + b + "=" + str(c))
# print("{}+{}={}".format(a, b, c))
print("%s+%s=%d" % (a, b, c))
# 传统的填充方式 %s代表填充字符串，%d代表填充整数，%f代表填充浮点数 %.2f代表填充浮点数，保留两位
str7 = "%s学校前段时间来了%d只大花猫，最近生了两只小%s" % ("学校", 1, "白猫")
print(str7)  # 学校学校前段时间来了1只大花猫，最近生了两只小白猫

str8 = "小猫每天长%f斤肉，%d天就能长2斤肉" % (0.22222, 10)
print(str8)  # 小猫每天长0.222220斤肉，10天就能长2斤肉

str9 = "小猫每天长%.2f斤肉，%d天就能长2斤肉" % (0.226892, 10)
print(str9)  # 小猫每天长0.23斤肉，10天就能长2斤肉

# 字符串的转义： 在python里 \n代表换行  \t 代表制表符 相当于一个tab
path = "c:\name\table.txt"
print(path)
"""
打印结果：
c:
ame	able.txt
"""
# 关闭转义：可以在字符串前面加   r/R
path = r"c:\name\table.txt"
print(path)  # c:\name\table.txt
