"""
============================
Author:柠檬班-木森
Time:2020/7/28   20:23
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


def login_check(username=None, password=None):
    """
    登录校验的函数
    :param username: 账号
    :param password:  密码
    :return: dict type
    """
    if username != None and password != None:
        if username == 'python31' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有的参数不能为空"}


"""
登录功能校验函数:
入参：username,password
出参（返回值）：{"code":业务码,"msg":"提示信息"}
内部校验逻辑，账号密码是否为空，账号密码是否正确
默认账号为：python27 ,密码：lemonban


1、账号密码正确 
入参：账号python27  密码lemonban     
预期结果：{"code": 0, "msg": "登录成功"}
实际结果：

2、账号正确，密码错误   
入参：账号python27  密码lemonban11     
预期结果：{"code": 1, "msg": "账号或密码不正确"}
实际结果：

3、账号错误，密码正确，
入参：账号python25  密码lemonban     
预期结果：{"code": 1, "msg": "账号或密码不正确"}
实际结果：

4、账号为空
入参：账号为空  密码lemonban11     
预期结果：{"code": 1, "msg": "所以的参数不能为空"}
实际结果：

5、密码为空、
入参：账号Python6  密码为空    
预期结果：{"code": 1, "msg": "所以的参数不能为空"}
实际结果
"""

if __name__ == '__main__':
    # ---------------------------1------------------------------
    # 测试函数正常登录
    # 第一步准备用例数据
    expected = {"code": 0, "msg": "登录成功"}
    data = ("python31", "lemonban")
    # 第二步：传入参数，获取实际结果
    res = login_check(*data)
    # 第三步：判断用例是否通过（比对预期结果和实际结果）
    if res == expected:
        print("用例执行通过！")
    else:
        print("用例执行失败！")
    # ----------------------------2----------------------------
    # 测试函数传入错误密码的情况
    expected2 = {"code": 1, "msg": "账号或密码不正确"}
    data2 = ("python31", "lemonban777")
    # 第二步：传入参数，获取实际结果
    res = login_check(*data)
    # 第三步：判断用例是否通过（比对预期结果和实际结果）
    if res == expected:
        print("用例执行通过！")
    else:
        print("用例执行失败！")
