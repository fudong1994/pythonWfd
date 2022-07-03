# print('我是伍福东' * 10)

import random

#
# sum = 0
# for i in range(3):
#     int1 = random.randint(1,6)
#     sum += int1
# print(sum)

# 有小红，小花，小妹，小张四个妹子，你现在有一次表白的机会，只有跟小花表白可以成功，其他妹子均会拒绝，设计代码，执行后打印表白结果

mm = ["小红", "小花", "小妹", "小张"]

con = random.choice(mm)
print(con)
if con == '小花':
    print("{}说：亲爱的，我也钟意你".format(con))
else:
    print(f"{con}说:不好意思，我不喜欢你")

while True:
    res = input("请选择一个妹子表白：\n")
    if res in ("小红", "小花", "小妹", "小张"):
        if res == '小花':
            print("亲爱的，我也钟意你")
            break
        else:
            print("滚犊子")
            break
    else:
        print("你选择的妹子不存在，请重新选择")
        continue
