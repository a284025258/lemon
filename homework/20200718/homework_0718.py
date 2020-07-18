"""
文件操作和模块导入
第一题：当前有一个txt文件，内容如下：

第二题：当前有一个case.txt文件，里面中存储了很多用例数据: 如下，每一行数据就是一条用例数据，

# 文件中数据
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
​
# 要求一： 请把这些数据读取出来，到并且存到list中，格式如下
[
{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
]
# 要求二：将上述数据再次进行转换，转换为下面这种字典格式格式
​
{
   'data1':{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
   'data2':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
   'data3':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
   'data4':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
   'data4':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
}
​
# 提示：需要使用字符串的分割方法
# 注意点：数据中如果有换行符'\n'，要想办法去掉。

第三题：之前上课讲了一个注册功能的案例，再之前案例的功能上进行升级，
要求：把所有用户数据放到文件中进行保存，数据存储的格式不限，原来的案例代码如下
users = [
    {"uid": "py01", "pwd": "lmb01"},
    {"uid": "py02", "pwd": "lmb02"},
]

id = input("请输入账号：")
pwd = input("请输入密码：")
pwd2 = input("请再次确认密码：")
# 遍历所有的账号
for u in users:
# 判断账号是否已经被注册
    if id == u["uid"]:
print("该账号已经被注册！")
break
else:
# 如果账号没有注册，那么for循环中的break不会执行。则会执行for对应的else语句
    print("该账号可以注册，继续判断密码！")
# 判断两次密码是否一致
    if pwd == pwd2:
print("注册成功！")
# 帮输入的账号密码已字典的形式加入道users中
        users.append({"uid": id, "pwd": pwd})
else:
print("两次输入的密码不一致")

提示：
每次运行程序，先去文件中读取所有注册过的用户数据，
程序运行完之后，将所有的用户数据再次写入到文件
可以把保存账号的列表转为字符串直接写入文件，读出来的时候，再把字符串转换为列表
"""
print("----------------------------第1题----------------------------")


def func1(file):
    dict1 = {}
    with open(file, 'r', encoding='utf8') as f1:
        list1 = f1.readlines()
        for i in range(len(list1)):
            list1[i] = list1[i].replace('\n', '')
            dict1['data' + str(i)] = list1[i]
    return dict1


print(func1(r"./data.txt"))

print("----------------------------第2题----------------------------")


def func2(file):
    dict2 = {}
    li1 = []
    li2 = []
    with open(file, 'r', encoding='utf8') as f2:
        list2 = f2.readlines()
        for i in range(len(list2)):
            list2[i] = list2[i].replace('\n', '').split(',')
            for j in range(len(list2[i])):
                li1.append(tuple(list2[i][j].split(':')))
            li2.append(dict(li1))
    print('----------------------------第1次格式化----------------------------')
    print(li2)
    print('----------------------------第2次格式化----------------------------')
    for i in range(len(li2)):
        dict2['data' + str(i + 1)] = li2[i]
    return dict2


print(func2(r"./case.txt"))

print("----------------------------第3题----------------------------")


def register(file):
    with open(file, 'r', encoding='utf8') as f3:
        users = eval(f3.readline())
        id = input("请输入账号：")
        pwd = input("请输入密码：")
        pwd2 = input("请再次确认密码：")
        # 遍历所有的账号
        for u in users:
            # 判断账号是否已经被注册
            if id == u["uid"]:
                print("该账号已经被注册！")
                break
        else:
            # 如果账号没有注册，那么for循环中的break不会执行。则会执行for对应的else语句
            print("该账号可以注册，继续判断密码！")
            # 判断两次密码是否一致
            if pwd == pwd2:
                print("注册成功！")
                # 帮输入的账号密码已字典的形式加入道users中
                users.append({"uid": id, "pwd": pwd})
                with open(file, 'w', encoding='utf8') as f4:
                    f4.write(str(users))
            else:
                print("两次输入的密码不一致")


register(r'user.txt')
