

class Hero:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def speak(self):
        print(f"当前英雄{self.name}的血量为{self.hp}，攻击力为{self.power}")

    def figh(self, enemy_name, enemy_hp, enemy_power):
        """
        对打。需要输入敌人的 名称， hp， power
        :return:
        """
        # 获取当前英雄的最终血量
        # 实例属性的作用域是整个类，其他方法也可以使用实例属性
        my_final_hp = self.hp - enemy_power
        # 获取"敌人"的最终血量
        enemy_final_hp = enemy_hp - self.power
        print(f"一轮对打过后，射手{self.name}的血量为{my_final_hp}，敌人{enemy_name}的血量为{enemy_final_hp}")
        if my_final_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif enemy_final_hp > my_final_hp:
            print(f"敌人{enemy_name}赢了")
        else:
            print("平局")


class Sam(Hero):
    """
    攻击力与血量在初始化的时候会发生变化
    """
    def __init__(self, name, hp, power):
        # self.name = name
        # self.hp = 0.8*hp
        # self.power = 1.2*power
        # 使用super()继承父类
        super().__init__(name, 0.8*hp, 1.2*power)


if __name__ == '__main__':
    # diaochan = Hero("貂蝉", 20, 100)
    # diaochan.speak()
    luban = Sam("鲁班", 200, 150)
    # luban.speak()
    luban.figh("王昭君", 200, 150)