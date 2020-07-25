"""
1、通过继承定义如下三个类：PhoneV1,PhoneV2,PhoneV3
   PhoneV1：
        类属性：attr = "移动电话",
             实例属性 name(品牌型号),price(价格),（year）生产年份
        方法：打电话

   PhoneV2：
        类属性：attr = "移动电话"，
        实例属性 name(品牌型号),price(价格),（year）生产年份， 摄像头像素(pixel)
             方法：打电话 ,听音乐，发短信，拍照

   PhoneV3：
        类属性：attr = "移动电话"
             实例属性 name(品牌型号),price(价格),（year）生产年份， 摄像头像素(pixel),屏幕大小(screen)
             方法：打电话 ,听音乐，发短信，拍照, 看视频



2、有一组数据，如下格式：
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},

定义一个如下的类，
请通过setattr将上面字典中的键值对，分别设置为类的属性和属性值，
键作为属性名，对应的值作为属性值
class CaseData:
    pass
"""

# ----------------------------第1题----------------------------


class PhoneV1(object):
    attr = "移动电话"

    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def call(self):
        print(f"{self.name} 可以打电话")


class PhoneV2(PhoneV1):
    def __init__(self, name, price, year, pixel):
        super().__init__(name, price, year)
        self.pixel = pixel

    def listen_music(self):
        print(f"{self.name} 可以听音乐")

    def send_msg(self):
        print(f"{self.name} 可以发短信")

    def take_picture(self):
        print(f"{self.name} 可以拍照")


class PhoneV3(PhoneV2):
    def __init__(self, name, price, year, pixel, screen):
        super().__init__(name, price, year, pixel)
        self.screen = screen

    def watch_video(self):
        print(f"{self.name} 可以看视频")


# ----------------------------第2题----------------------------
class CaseData:
    pass


if __name__ == "__main__":
    data = {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'}
    for key in data:
        setattr(CaseData, key, data[key])
    print(CaseData.__dict__)
