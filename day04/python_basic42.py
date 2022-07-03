"""
# @Time : 2022/5/8 0008 11:33
# @File : python_basic42
# @Project : pythonWfd
# @Content :
"""

"""
本章讲解：多分支条件判断
语法：
if 条件1：
    语句块1
elif 条件2：
    语句块2
elif 条件3：
    语句块3
.....
[else：
    语句块4]

"""

# 0-6岁婴儿，7-12岁为少儿，13-17岁为青少年，18-45岁为青年，46-69岁为中年，大于69岁老年
age = int(input('请输入年龄：'))

if 0 < age <= 6:
    print('婴幼儿阶段，好好玩耍')
elif 6 < age <= 12:
    print('好好学习天天向上')
elif 12 < age <= 17:
    print('青少年阶段,学习')
elif 17 < age <= 45:
    print('努力拼搏，争取老板明年换车')
elif 45 < age <= 69:
    print('带娃，享受生活')
else:  # 如果以上所有的情况都不满足，执行else下的语句块
    print('老年阶段，好好活着')


code1 = input('对暗号--天王盖地虎：')
if code1 == "宝塔镇河妖":
    code2 = input("请继续对暗号--小鸡炖蘑菇：")
    if code2 == "蘑菇放辣椒":
        print("自己人，请进来")
    else:
        print("来人，拖出去砍了！")
else:
    print("来人，拖出去砍了！")


code3 = int(input("开始测试酒精含量："))
if code3 < 20:
    print("不构成饮酒行为")
elif 20 <= code3 < 80:
    print("已经达到饮酒驾驶标准")
else:
    print("已经达到醉酒驾驶标准")
