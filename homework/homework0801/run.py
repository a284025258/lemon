import unittest
from unittestreport import TestRunner
from homework.homework0801 import test_case


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_case)
    # suite = unittest.defaultTestLoader.discover(r"./")
    runner = TestRunner(suite=suite, tester="小石头", desc="小石头的测试报告")
    runner.run()
