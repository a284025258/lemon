import os
import random


"""
1、实现一个文件复制器函数，通过给函数传入一个路径，复制该路径下面所有的文件(目录不用复制)到当前目录，
要求：如果传路径不存在，不能报错                提示：os模块结合文件读写操作 、异常捕获 即可实现

2、优化之前作业的石头剪刀布游戏，用户输入时，如果输入非数字会引发异常，请通过异常捕获来处理这个问题。
"""


def copy_file(file_path):
    try:
        # 获取路径下所有文件名称
        file_list = os.listdir(file_path)
        for i in file_list:
            # 遍历并拼接文件路径
            file = os.path.join(file_path, i)
            # 判断是否为文件
            if os.path.isfile(file):
                # 读取文件
                with open(file=file, mode='rb') as f1:
                    content = f1.read()
                # 写入当前目录
                with open(file=rf'./cp_{i}', mode='wb') as f1:
                    f1.write(content)
                    print(f'已复制文件：{i}')
    except FileNotFoundError as e:
        print(e)


def play():
    print("欢迎游玩【剪刀石头布】游戏！")
    list1 = ['石头', '剪刀', '布']
    while True:
        try:
            player = int(input("请输入您要出的拳 ：石头【1】 剪刀【2】 布【3】 退出【4】\n"))
            if player in [1, 2, 3, 4]:
                if player == 4:
                    break
                computer = random.randint(1, 3)
                # player_win = [(1, 2), (2, 3), (3, 1)]  # -1 2
                # player_lose = [(1, 3), (2, 1), (3, 2)]  # -2 1
                # player_draw = [(1, 1), (2, 2), (3, 3)]  # 相等

                if player == computer:
                    print(f"您出的是【{list1[player - 1]}】, 电脑出的是【{list1[computer - 1]}】, 平局！")
                elif player - computer == -1 or player - computer == 2:
                    print(f"您出的是【{list1[player - 1]}】, 电脑出的是【{list1[computer - 1]}】, 恭喜您，您赢啦！！！")
                elif player - computer == 1 or player - computer == -2:
                    print(f"您出的是【{list1[player - 1]}】, 电脑出的是【{list1[computer - 1]}】, 很遗憾，您输了。。。")
            else:
                print("选择有误，只能选择1-4！")
        except ValueError:
            print('输入有误，只能输入数字！')
    print("游戏结束！下次再来玩儿哦！")


if __name__ == '__main__':
    print("----------------------------第1题----------------------------")
    copy_file(r'D:\pychram_workspace\lemon_homework\homework\20200702')
    print("----------------------------第2题----------------------------")
    play()
