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
"""

import unittest
from unittestreport import TestRunner
from register import register


class TestRegister(unittest.TestCase):
    def test_register_01(self):
        """帐号和密码均为空"""
        user = {"username": None, "password1": None, "password2": None}
        expected = {"code": 0, "msg": "所有参数不能为空"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_02(self):
        """帐号为空"""
        user = {"username": None, "password1": "123456", "password2": "123456"}
        expected = {"code": 0, "msg": "所有参数不能为空"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_03(self):
        """密码为空"""
        user = {"username": "user123", "password1": None, "password2": None}
        expected = {"code": 0, "msg": "所有参数不能为空"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_04(self):
        """密码小于6位"""
        user = {"username": "user123", "password1": "12345", "password2": "12345"}
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_05(self):
        """密码大于18位"""
        user = {"username": "user123", "password1": "1234567890123456789", "password2": "1234567890123456789"}
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_06(self):
        """帐号已注册"""
        user = {"username": "python31", "password1": "123456", "password2": "123456"}
        expected = {"code": 0, "msg": "该账户已存在"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_07(self):
        """两次密码不一致"""
        user = {"username": "python32", "password1": "1234567", "password2": "123456"}
        expected = {"code": 0, "msg": "两次密码不一致"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_08(self):
        """帐号小于6位"""
        user = {"username": "user1", "password1": "123456", "password2": "123456"}
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_09(self):
        """帐号大于18位"""
        user = {"username": "user123456789012345", "password1": "123456", "password2": "123456"}
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        result = register(**user)
        self.assertEqual(expected, result)

    def test_register_10(self):
        """正常注册"""
        user = {"username": "admin1", "password1": "123456", "password2": "123456"}
        expected = {"code": 1, "msg": "注册成功"}
        result = register(**user)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestRegister))
    runner = TestRunner(suite=suite, tester="小石头", desc="小石头的测试报告")
    runner.run()
