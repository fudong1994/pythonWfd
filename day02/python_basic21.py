# @Time : 2022/4/23 11:10
# @File : python_basic21
# @Project : pythonWfd
# @Content : 运算符

# 知识点1：算术运算符 + - *(乘) /(除) %(取余) //(向下取整) **(幂等)
a, b = 10, 20
print(a + b)  # 30
print(a - b)  # -10
print(a * b)  # 200
print(a / b)  # 0.5
print(10 / 3)  # 3.3333333333333335 浮点数的计算，四舍五入
print(a % b)  # 10 取余数
print(a // b)  # 0 向下取整，特地是保留整数位
print(a ** 2)  # 100 幂等 就是N次方

# %代表取余数
print(4 % 2)  # 0
print(6 % 4)  # 2
print(7 % 5)  # 2

# 1.小对大取余数 结果余小的
print(1 % 2)  # 1
print(3 % 5)  # 3

# 2、能够整除，余数为0
print(10 % 2)  # 0
print(6 % 3)  # 0

# 3、偶数对2取余数，结果为0，奇数对2取余数，结果为1
print(1 % 2)  # 1
print(2 % 2)  # 0
print(3 % 2)  # 1
print(4 % 2)  # 0
print(5 % 2)  # 1
print(6 % 2)  # 0

# //代表 向下取整，只保留整数位
print(10 // 3)  # 3

# 幂等 就是N次方
print(2 ** 2)  # 4
print(2 ** 3)  # 8
print(3 ** 3)  # 27

# 知识点2：赋值运算符 =  +=  -=  *=  /=  %=  //=
name = "小花"
print(name == "小花")  # True  ==判断两边是否相等
a = 10
a += 10  # 相当于 a = a+10
a -= 10  # a = a-10,a的值为10
a *= 5  # a的值为50
a /= 10  # a的值为5
a %= 3  # a的值为2
a **= 2  # a的值为4
print(a)  # 4

# 比较运算符   >    <    >=   <=    !=(不等于)   ==(相等)  结果只能是 True或False
a, b = 10, 20
print(a >= b)  # False
print(a == b)  # False
print(a != b)  # True !=判断两边是否不相等，如果不相等返回True

# 逻辑运算符 and(并且)    or(或者)  not(取反)
# and 多个条件连接的时候，所有成立整个表达式成立，有一个不成立结果为False，全真为真
a, b = 10, 20
print(a == b and a > b)  # False
print(a != b and a < b)  # True

# or 多个条件连接的时候，有一个成立表达式成立，只有所有的不成立，表达式才不成立，全假为假
print(a == b or a > b)  # False
print(a == b or a < b)  # True

# 逻辑运算符 not 代表取反
print(not False)  # True
print(not True)  # False
print(not a == b)  # True
print(not (a == b or a > b))  # True

# 成员运算符 in、 not in
print("x" in 'python')  # False
print("x" not in 'python')  # True
print(2 in [1, 2, 3])  # True
