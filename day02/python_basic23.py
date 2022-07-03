"""
# @Time : 2022/4/23 0023 16:14
# @File : python_basic23
# @Project : pythonWfd
# @Content : 字符串相关API
"""
# 1、len() 求字符串长度 length的缩写（长度）
name = "小花"
print(len(name))

# 字符串长度和最大下标的关系 字符串长度-1 = 最大下标
# print(name[2]) # IndexError: string index out of range 下标越界错误

# 2、字符串内容的替换 str.replace(a,b) 会把str中的 a 替换成 b
str1 = "疫情很快会过去的！"
str2 = str1.replace("的", "吧")
print(str2)  # 疫情很快会过去吧！

# 练习：去除字符串中所有的空格"abcdef g h i j kht"

str3 = "abcdef g h i j kht"
str4 = str3.replace(" ", "")
print(str4)

# 字符串find() 查找字符串中元素第一次出现的位置
str5 = "i like python"
index = str5.find("i")
print(index)  # 0
index = str5.find("C")
print(index)  # -1 找不到的返回-1

# join拼接
str6 = "-".join("123456")
print(str6)  # 1-2-3-4-5-6

# count 统计元素在字符串中出现的次数
str7 = "i like python"
print(str7.count("i"))  # 2
print(str7.count("p"))  # 1
print(str7.count("c"))  # 0  不存在结果为0

# upper将字符串转为大写/lower将字符串转为小写
print("I Like Python".upper())  # I LIKE PYTHON
print("I Like Python".lower())  # i like python

# isnumeric() 判断字符串是否为数字类型的字符串,如果是返回True 反之返回False
print("12345".isnumeric())  # True
print("1234a".isnumeric())  # False

# 案例

a = input("请输入第一个数：\n")
b = input("请输入第二个数：\n")
if a.isnumeric() and b.isnumeric():
    c = int(a) + int(b)
    print(a + "+" + b + "=" + str(c))
else:
    print("请输入数字")

# 切分字符串 字符串可以进行切分，切分后返回列表
lst1 = "2018-10-20".split("-")
print(lst1)  # ['2018', '10', '20']
# 获取当前时间的分钟数
lst2 = "17:24:20".split(":")
print(lst2)  # ['17', '24', '20']
print(lst2[1])  # 24  获取列表下标为1的值

lst3 = "12 34 5".split()  # 默认按空格切分
print(lst3)  # ['12', '34', '5']

print(''.join("12 34 5".split()))

# 1、把列表转为字符串[1,2,3,4,5],12345
lst4 = [1, 2, 3, 4, 5]
# 方法1：列表转换为字符串后进行替换
str8 = str(lst4).replace("[", "").replace("]", "").replace(", ", '')
print(str8)

# 方法2：遍历列表，转换为str类型后进行拼接
str10 = ""
for i in lst4:
    str10 += str(i)
print(str10)

# 方法3：map函数
print(''.join(map(str, lst4)))

# 方法4：遍历后转换为str类型后塞到新的列表在用join进行转换
lst5 = []
for i in lst4:
    lst5.append(str(i))
print(''.join(lst5))
