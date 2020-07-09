import random
'''
1、现在有变量 a = ‘hello’ ,    b = ‘python18’     c = ‘!’  ,通过相关操作变成一个字符串：'hello python18 !'（注意点:转换之后单词之间有空格）

2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格（整数），然后随机生成购买的斤数（5到10斤之间的整数），最后打印出应该支付的金额！

3、请随机生成一个131开头的手机号码。

4、 请定义一个字符串，并通过print打印字符串，打印出来字符串的内容如下    PHP is the best""" \tprogramming"language in 'the\norld
'''

# 1、现在有变量 a = ‘hello’ ,    b = ‘python18’     c = ‘!’  ,通过相关操作变成一个字符串：'hello python18 !'（注意点:转换之后单词之间有空格）
a = 'hello'
b = 'python18'
c = '!'
string1 = f'{a} {b} {c}'
print(string1)

# 2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格（整数），然后随机生成购买的斤数（5到10斤之间的整数），最后打印出应该支付的金额！

price = int(input('输入橘子的价格（整数）：'))
weight = random.randint(5, 10)
total = price * weight
print(f'单价：{price}，重量：{weight}，应支付金额：{total}')

# 3、请随机生成一个131开头的手机号码。
tele_number = random.randint(13100000000, 13199999999)
print(tele_number)

# 4、 请定义一个字符串，并通过print打印字符串，打印出来字符串的内容如下    PHP is the best""" \tprogramming"language in 'the\norld

string2 = "PHP is the best\"\"\" \\tprogramming\"language in 'the\\norld"
print(string2)


