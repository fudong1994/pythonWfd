"""
# @Time : 2022/5/8 0008 19:26
# @File : python_basic44
# @Project : pythonWfd
# @Content :
"""

"""
1.死循环
2.while循环使用else语句： 在while...else,当循环判定条件为False时执行else语句块
3.终止循环用break
4.跳过本次循环使用continue
"""

"""
常见的死循环：

# 案例1
i = 1
while i <= 100:
    print(i)

# 案例2：
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
        i += 1
"""

i = 1
while i <= 10:
    print(i)
    i += 1
else:  # 循环结束后，执行else下的代码
    print('循环结束')

print('===' * 50)

i = 0
while i <= 10:
    i += 1
    if i == 5:
        # break  # 打印结果：1、2、3、4  当i=5的时候整个循环终止
        continue  # 当i=5的时候，跳过本轮循环，不执行下面代码，执行下轮循环
    print(i)

print('Hello')

count = 0
while True:
    name = input('请输入用户名：')
    password = input('请输入密码：')
    count += 1

    if name == 'scott' and password == '123456':
        print('登录成功')
        break
    if count == 3:
        print('您输入错误次数过多,请稍后重试!')
        break
