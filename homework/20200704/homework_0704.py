"""
一、现在有一个列表 li2=[1，2，3，4，5]，

     第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，
     第二步：对列表进行升序排序 （从小到大）
     第三步：将列表复制一份进行降序排序（从大到小）

二、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，
    将输入的信息作为添加的列表中保存，然后按照一下格式输出：
    用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对

三、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
（提示：通过字符串分割，拼接，列表反序等知识点来实现）



四、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
        1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
        2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
        3、平台需要补足您的身高和联系方式；（分别输入身高和联系方式添加到字典中）
        4、平台为了保护你的隐私，需要你删除你的联系方式（删除字典中的联系方式）；
"""

print("----------------------------第1题----------------------------")
li2 = [1, 2, 3, 4, 5]
# 第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]
li2.insert(0, 0)
li2[4] = 66
li2.extend([11, 22, 33])
# 对列表进行升序排序 （从小到大）
li2.sort()
# 将列表复制一份进行降序排序（从大到小）
li2_copy = li2.copy()
li2_copy.sort(reverse=True)
print(f"{li2} \n{li2_copy}")
print("----------------------------第2题----------------------------")
user = []
# 分别提示用户输入，姓名，年龄，身高
name = input("请输入姓名：")
age = input("请输入年龄：")
stature = input("请输入身高(单位：cm)：")
user.append(name)
user.append(age)
user.append(stature)
print(f"用户的姓名为：{user[0]},年龄为：{user[1]},  身高为：{user[2]}  ,请仔细核对")
print("----------------------------第3题----------------------------")
str1 = "hello xiao mi"
list1 = str1.split(' ')
list1.reverse()
str2 = ' '.join(list1)
print(str2)
print("----------------------------第4题----------------------------")
# 运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来
name_dic = input("请输入姓名：")
gender_dic = input("请输入性别：")
age_dic = input("请输入年龄：")
user_dic = dict(name=name_dic, gender=gender_dic, age=age_dic)
# 数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
print(f"我的名字{user_dic['name']}，今年{user_dic['age']}岁，性别:{user_dic['gender']}，喜欢敲代码")
# 平台需要补足您的身高和联系方式；（分别输入身高和联系方式添加到字典中）
stature_dic = input("请输入身高：")
telephone_dic = input("请输入联系方式：")
user_dic['stature'] = stature_dic
user_dic['telephone'] = telephone_dic
# 平台为了保护你的隐私，需要你删除你的联系方式（删除字典中的联系方式）
user_dic.pop('telephone')
print(user_dic)


