"""
函数的参数及内部代码逻辑：
函数入参：
注意：参数传字符串类型，不需要考虑其他类型。
参数1：账号
参数2：密码1
参数2：密码2


函数内部处理的逻辑：
   判断是否有参数为空，
    判断账号密码是否在6-18位之间，
    判断账号是否被注册过，
    判断两个密码是否一致。
    上面添加都校验通过才能注册成功，其他情况都注册失败，
各种情况的返回结果如下：
  注册成功               返回结果：{"code": 1, "msg": "注册成功"}
   有参数为空，            返回结果 {"code": 0, "msg": "所有参数不能为空"}
   两次密码不一致          返回结果：{"code": 0, "msg": "两次密码不一致"}
   账户已存在             返回结果：{"code": 0, "msg": "该账户已存在"}
   密码不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
   账号不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}


作业要求：请设计用例（不少5条），对此功能函数进行测试，

提示：上面已经被注册的账号：python31
提示：不需要去看功能函数内部的代码是怎么实现的，也不要改里面的代码，直接复制过去就好，函数内部有bug,自己设计用例去测，测到了自己记录下来


优化上次作业，
要求：将用例数据存放在excel中，读取excel中的用例数据，并使用ddt来实现数据驱动！
注意点：上课最后五分钟讲的细节别忘了，excel中读取出来的字典和列表的数据类型是字符串，需要使用eval来转换

作业要求：按照上课进度，讲前面做的login_check和register这两个功能函数的代码进行优化！实现结果回写excel!
"""
import unittest
from unittestreport import TestRunner
from .register import register
from .login import login_check
from .ddt import data, ddt
from .read_excel import ReadExcel


@ddt
class TestRegister(unittest.TestCase):
    """注册用户测试用例类"""
    read_excel = ReadExcel(filename=r"./cases.xlsx", sheet_name="register")
    cases = read_excel.read_data()
    @data(*cases)
    def test_register(self, case):
        result = register(**eval(case["param"]))
        try:
            self.assertEqual(eval(case["expected"]), result)
            self.read_excel.write_data(case["case_id"] + 1, 6, "已通过")
        except (AssertionError, Exception) as e:
            if isinstance(e, AssertionError):
                self.read_excel.write_data(case["case_id"] + 1, 6, "未通过")
            else:
                self.read_excel.write_data(case["case_id"] + 1, 6, "Error")
            raise e


@ddt
class TestLogin(unittest.TestCase):
    """用户登录测试用例类"""
    read_excel = ReadExcel(filename=r"./cases.xlsx", sheet_name="login")
    cases = read_excel.read_data()
    @data(*cases)
    def test_register(self, case):
        result = login_check(**eval(case["param"]))
        try:
            self.assertEqual(eval(case["expected"]), result)
            self.read_excel.write_data(case["case_id"] + 1, 6, "已通过")
        except (AssertionError, Exception) as e:
            if isinstance(e, AssertionError):
                self.read_excel.write_data(case["case_id"] + 1, 6, "未通过")
            else:
                self.read_excel.write_data(case["case_id"] + 1, 6, "Error")
            raise e


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(r"./")
    runner = TestRunner(suite=suite, tester="小石头", desc="小石头的测试报告")
    runner.run()
