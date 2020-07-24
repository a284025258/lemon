"""
1、类属性怎么定义？ 实例属性怎么定义(简答)？

2、实例方法中的self代表什么？（简答）


3、类中__init__方法在什么时候会调用？（简答）


4、封装一个学生类，(自行分辨定义为类属性还是实例属性)
    属性：，身份(学生) 姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
    方法一：计算总分，
    方法二：计算三科平均分，
    方法三：打印学生的个人信息。

5、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，
    属性：用例编号  url地址   请求参数   请求方法    预期结果   实际结果
"""

print("----------------------------第1题----------------------------")
print("类属性怎么定义？ 实例属性怎么定义(简答)？")
print("""
答：
类属性：直接定义在类里面的变量
实例属性：1、在__init__()初始化方法内定义 self.属性名 = 属性值
        2、创建对象后，对象名.属性名 = 属性值
""")

print("----------------------------第2题----------------------------")
print("2、实例方法中的self代表什么？（简答）")
print("答：self 代表对象本身")

print("----------------------------第3题----------------------------")
print("3、类中__init__方法在什么时候会调用？")
print("答：创建对象时调用")

print("----------------------------第4题----------------------------")


class Student():
    identity = "student"

    def __init__(self, name, age, gender, english_grade, math_grade, chinese_grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.english_grade = english_grade
        self.math_grade = math_grade
        self.chinese_grade = chinese_grade

    def sum_grade(self):
        return self.english_grade + self.math_grade + self.chinese_grade

    def avg_grade(self):
        return (self.english_grade + self.math_grade + self.chinese_grade) / 3

    def print_info(self):
        print(f"name:{self.name} age:{self.age} gender:{self.gender}")


print("----------------------------第5题----------------------------")


class TestCase():
    url = 'https://www.xxx.com/login'
    method = 'post'

    def __init__(self, case_id, param,  expected, result):
        self.case_id = case_id
        self.param = param
        self.expected = expected
        self.result = result


if __name__ == "__main__":
    student1 = Student('Jax', 18, '男', 99, 98, 87)
    print("三科总分为：", student1.sum_grade())
    print("三科平均分为：{:.2f}".format(student1.avg_grade()))
    student1.print_info()
