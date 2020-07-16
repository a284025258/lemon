"""
第一题：请封装一个函数，按要求实现数据的格式转换
# 传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# 返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
# 通过代码将传入参数转换为返回结果所需数据，然后返回

第二题：请封装一个函数，完成如下数据格式转换
传入参数：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

# 返回结果
cases02 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]

第三题：简单题
#  1、什么是全局变量？
#  2、什么是局部变量？
#  3、函数内部如何修改全局变量（声明全局变量 ）？
"""


print("----------------------------第1题----------------------------")


def conversion(data):
    res = []
    for i in data:
        res.append(eval(i))
    return res


data = ["{'a':11,'b':2}", "[11,22,33,44]"]
res = conversion(data)
print(res)

print("----------------------------第2题----------------------------")


def conversion2(cases):
    cases02 = []
    for i in range(1, len(cases)):
        cases02.append(dict(zip(cases[0], cases[i])))
    return cases02


cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
print(conversion2(cases))

print("----------------------------第3题----------------------------")
print('1、什么是全局变量？')
print('答：定义在模块中的变量')
print('2、什么是局部变量？')
print('答：定义在函数中的变量')
print('3、函数内部如何修改全局变量（声明全局变量 ）？')
print('答：使用 global 关键字在函数内部声明全局变量')
