
from fight_game.fight import Sam
# 主入口

# 模块与包

# 是否在当前模块执行的
if __name__ == '__main__':
    hero_name = input("请输入英雄的名称：")
    hero_hp = input("请输入英雄的血量：")
    hero_power = input("请输入英雄的攻击力：")
    # diaochan = Hero("貂蝉", 20, 100)
    # diaochan.speak()
    luban = Sam(hero_name, int(hero_hp), int(hero_power))
    # luban.speak()
    luban.figh("王昭君", 200, 150)
