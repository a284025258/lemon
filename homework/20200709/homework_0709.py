"""
1、实现剪刀石头布游戏（），提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4） 电脑随机出拳比较胜负，显示 用户胜、负还是平局。
运行如下图所示（提示：while循环加条件判断，做判断时建议先分析胜负的情况）
user   random
1        2     1-2 =-1
2        3     2-3= -1
3        1     3- 1 = 2

2、通过定义一个计算器，允许程序提示用户输入数字1，数字2，然后再提示用户选择 ：
 加【1】    减【2】    乘【3】      除【4】，
根据不同的选择完成不同的计算 ，然后打印结果

3、请获取下面字典数据中的token，和reg_name
data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
4、当前有一个列表 li = [1,21,33,221,432,121,44,21,22,,44,1,221],请完成如下要求！
1、请先去除列表中的重复元素
2、对去重后的列表进行升序排序
3、遍历排序后列表，将元素为偶数的元素，添加到一个新列表中
第5题、运行程序，提示用户依次输入三个整数x,y,z，请把这三个数由小到大输出。
第6题、编写一个程序，使用for循环输出0-100（包括0和100）之间的偶数
第7题、当前有一个字典｛"a":1,"b":22,"c":3,"d":4,"e":5 },请修改字典中所有键值对的值，新的值为原来的值乘10

二、扩展题（选做）
温馨提示：难度系数偏高做不出来没关系
1、题目：企业发放的奖金根据利润提成（提示：用到的知识点：条件判断）
用户输入利润

利润低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时，高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于
100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

2、编写一个文字版的自动售货机的代码，运行功能如下:
提示：用到的主要知识点，条件判断 、while循环
1、运行程序打印如下提示，
请用输入您购买的商品编号：
【1】可乐 2.5元​ 【2】雪碧 2.5元​ 【3】哇哈哈 3元​ 【4】红牛 6元​ 【5】脉动 4元​ 【6】果粒橙 3.5元
2、用户输入选择之后，打印如下格式的提示：您购买的是XX，需要支付金额为XX元
3、打印：请投币（支持1元，5元，10元）
4、用户输入投币金额，判断用户输入金额是否大于商品价格
用户投币金额不够商品价格，继续提示投币，
当投币超过商品价格，则打印投币的金额和找零金额，然后结束程序

备注：第3题和第4题超纲了，不用去做，如果有看预习视频的同学可以尝试去做一下
3、打印99乘法表，结果如下：
4、小明有100块钱 ，需要买100本书（钱要刚好花完），a类数5元一本，b类书3元一本，c类书 1元2本。请写一段代码计算小明有多少种购买的方式？
思路提示：穷举法，使用技术点：for循环嵌套
"""

import random

print("----------------------------第1题----------------------------")
print("欢迎游玩【剪刀石头布】游戏！")
list1 = ['石头', '剪刀', '布']
while True:
    player = input("请输入您要出的拳 ：石头【1】 剪刀【2】 布【3】 退出【4】\n")
    if player in ['1', '2', '3', '4']:
        player = int(player)
        if player == 4:
            break
        computer = random.randint(1, 3)
        # player_win = [(1, 2), (2, 3), (3, 1)]  # -1 2
        # player_lose = [(1, 3), (2, 1), (3, 2)]  # -2 1
        # player_draw = [(1, 1), (2, 2), (3, 3)]  # 相等

        if player == computer:
            print(f"您出的是【{list1[player - 1]}】, 电脑出的是【{list1[computer - 1]}】, 平局！")
        elif player - computer == -1 or player - computer == 2:
            print(f"您出的是【{list1[player - 1]}】, 电脑出的是【{list1[computer - 1]}】, 恭喜您，您赢啦！！！")
        elif player - computer == 1 or player - computer == -2:
            print(f"您出的是【{list1[player - 1]}】, 电脑出的是【{list1[computer - 1]}】, 很遗憾，您输了。。。")
    else:
        print("您输入有误，请重新输入哦。")
print("游戏结束！下次再来玩儿哦！")

print("----------------------------第2题----------------------------")
number1 = float(input("请输入第1个数："))
number2 = float(input("请输入第2个数："))
while True:
    operation = input('请选择：加【1】    减【2】    乘【3】    除【4】\n')
    if operation not in ['1', '2', '3', '4']:
        print("您选择的操作有误, 请重新选择!")
    else:
        operation = int(operation)
        if operation == 1:
            print(f"您输入的第1个数为：{number1}, 您输入的第2个数为：{number2}, 您选择的操作是：【加】, 运算结果是：{number1 + number2}")
        elif operation == 2:
            print(f"您输入的第1个数为：{number1}, 您输入的第2个数为：{number2}, 您选择的操作是：【减】, 运算结果是：{number1 - number2}")
        elif operation == 3:
            print(f"您输入的第1个数为：{number1}, 您输入的第2个数为：{number2}, 您选择的操作是：【乘】, 运算结果是：{number1 * number2}")
        elif operation == 4:
            print(f"您输入的第1个数为：{number1}, 您输入的第2个数为：{number2}, 您选择的操作是：【除】, 运算结果是：{number1 / number2}")
        break

print("----------------------------第3题----------------------------")
data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
print(f'reg_name: {data["data"]["reg_name"]}\ntoken: {data["data"]["token_info"]["token"]}')

print("----------------------------第4题----------------------------")
li = [1, 21, 33, 221, 432, 121, 44, 21, 22, 44, 1, 221]
print(f'原始列表：{li}')
# 去除列表重复元素
li = list(set(li))
print(f'去重后的结果：{li}')
# 升序排序
li.sort()
print(f'排序后的结果：{li}')
# 将元素为偶数的元素，添加到新列表
even_li = []
for i in li:
    if i % 2 == 0:
        even_li.append(i)
print(f'新列表为：{even_li}')

print("----------------------------第5题----------------------------")
print('请依次输入3个整数')
x = int(input('请输入第1个整数：\n'))
y = int(input('请输入第2个整数：\n'))
z = int(input('请输入第3个整数：\n'))
# 默认第一个数最大
max_number = x
# x， y 两者比较，如果 y 大，则将 y 赋值给 max_number
if x < y:
    max_number = y
# max_number，z 两者比较，如果 z 大，则将 z 赋值给 max_number
if max_number < z:
    max_number = z
    # x，y两者比较，则可直接判断三者大小关系
    if x > y:
        print(f'您输入的三个数从小到大依次为：{y} - {x} - {z}')
    else:
        print(f'您输入的三个数从小到大依次为：{x} - {y} - {z}')
# max_number，z 两者比较，如果 max_number 大，则继续比较 max_number 是 x 还是 y
elif max_number > z and max_number == x:
    # 若 max_number 是 x，则比较 y，z，则可判断三者大小
    if z > y:
        print(f'您输入的三个数从小到大依次为：{y} - {z} - {x}')
    else:
        print(f'您输入的三个数从小到大依次为：{z} - {y} - {x}')
elif max_number > z and max_number == y:
    # 若 max_number 是 x，则比较 x，z，则可判断三者大小
    if z > x:
        print(f'您输入的三个数从小到大依次为：{x} - {z} - {y}')
    else:
        print(f'您输入的三个数从小到大依次为：{z} - {x} - {y}')
# 若 max_number 与 z 相等
elif max_number == z:
    # 则比较 x，y，则可判断三者大小
    if x > y:
        print(f'您输入的三个数从小到大依次为：{y} - {x} - {z}')
    # 若 x，y，z 三者相等，则直接输出结果
    else:
        print(f'您输入的三个数从小到大依次为：{x} - {y} - {z}')

print("----------------------------第6题----------------------------")
print('0 - 100 的偶数为：')
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=' ')
print()
print("----------------------------第7题----------------------------")
dict7 = {"a": 1, "b": 22, "c": 3, "d": 4, "e": 5}
print('原始字典为：', dict7)
for k, v in dict7.items():
    dict7[k] = v * 10
print('修改后的字典为：', dict7)

print("----------------------------扩展题 第1题----------------------------")
while True:
    profits = float(input('请输入总利润：\n'))
    if 0 <= profits <= 100000:
        bonus = profits * 0.1
    elif 100000 < profits <= 200000:
        bonus = 100000 * 0.1 + (profits - 100000) * 0.075
    elif 200000 < profits <= 400000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + (profits - 200000) * 0.05
    elif 400000 < profits <= 600000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profits - 400000) * 0.03
    elif 600000 < profits <= 1000000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profits - 600000) * 0.015
    elif profits > 1000000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profits - 600000) * 0.01
    else:
        print('输入有误，请重新输入！')
        continue
    print('总利润为：{:.2f}, 奖金为：{:.2f}'.format(profits, bonus))
    break

print("----------------------------扩展题 第2题----------------------------")
goods_list = [{'可乐': '2.5'}, {'雪碧':'2.5'}, {'哇哈哈':'3'}, {'红牛': '6'}, {'脉动': '4'}, {'果粒橙': '3.5'}]
# 第1重循环：判断输入商品编号，是否在商品列表里
while True:
    goods_str = input('请输入您购买的商品编号：\n 【1】可乐 2.5元​ 【2】雪碧 2.5元​ 【3】哇哈哈 3元​ 【4】红牛 6元​ 【5】脉动 4元​ 【6】果粒橙 3.5元\n')
    # 输入商品编号，不在商品列表，则结束本次循环，重新输入商品编号
    if goods_str not in ['1', '2', '3', '4', '5', '6']:
        print('您选择有误，请重新选择！')
        continue
    # 输入商品编号，存在于商品列表，继续执行
    # 将商品编号转换为 int 类型
    goods = int(goods_str)
    # 获取输入商品的名称
    name = list(goods_list[goods - 1].items())[0][0]
    # 获取输入商品的价格
    price = float(list(goods_list[goods - 1].items())[0][1])
    print(f'您购买的是：【{name}】，需要支付金额为：【{price}】元')
    money = 0
    # 第2重循环：判断投币的金额是否支持
    while True:
        money_str = input('请投币（支持1元，5元，10元）:\n')
        # 投币的金额不支持，则退出本次循环，重新投币
        if money_str not in ['1', '5', '10']:
            print('您投币金额不支持，已退回！请重新投币。')
            continue
        # 投币的金额支持，继续执行
        # 将投币金额转换为 int 类型
        money += int(money_str)
        if money >= price:
            print('您投币总额为：{:.2f}元, 本次消费{:.2f}元，找零{:.2f}元！交易结束，欢迎下次再来！'.format(money, price, money - price))
            break
        else:
            print('您投币总额为{:.2f}元, 该商品的价格为{:.2f}, 不足以支付该商品，请继续投币。:\n'.format(money, price))
            continue
    break

print("----------------------------扩展题 第3题----------------------------")
print('九九乘法表：')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} x {i} = {i * j} \t', end='')
    print()

print("----------------------------扩展题 第4题----------------------------")
money4 = 100
price_a = 5
price_b = 3
price_c = 0.5
for a in range(int(money4 / price_a + 1)):
    for b in range(int(money4 / price_b + 1)):
        for c in range(int(money4 / price_c + 1)):
            if a + b + c == 100 and price_a * a + price_b * b + price_c * c == 100:
                print(f'可能的组合为：a类书买{a}本，b类书买{b}本， c类书买{c}本')
