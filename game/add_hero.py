
"""
1、实现英雄的删除功能
2、如果被删除的英雄不存在，则给出提示信息
3、函数
"""
print("""
1. **创建英雄**
2. **查看英雄信息**
3. **修改英雄信息**
4. **删除英雄**
5. **退出系统**
""")


def delete_hero(hero_list, hero_name):
    for i in hero_list:
    #     # 直到匹配到被查询的英雄
    #     # if 要查询的英雄信息 == 遍历的每英雄的名字
        if hero_name == i['name']:
            hero_list.remove(i)
            print(f"删除之后的英雄信息为{hero_list}")
            return hero_list
    print("没有可以删除的英雄")
    return hero_list


def update_hero(hero_list, hero_name):
    for i in hero_list:
        if hero_name == i["name"]:
            hero_list.remove(i)
            update_hero_name = input("请输入修改后的英雄姓名:")
            update_hero_volume = input("请输入修改后的英雄血量:")
            update_hero_power = input("请输入修改后的英雄攻击力:")
            hero_update_info = {"name": update_hero_name, "volume": update_hero_volume, "power": update_hero_power}
            print(f"修改的英雄名字为{update_hero_name}, 血量为{update_hero_volume}, 攻击力为{update_hero_power}")
            hero_list.append(hero_update_info)
            return hero_list
    print("没有可以修改的英雄")
    return hero_list


# 问题：按目前的实现，添加功能和查看都是针对的一个英雄
# 解决方案：将多个英雄数据保存下来 -> 列表
hero_list = []
while True:
    res = input("请输入对应的选项，即可执行对应的操作：")
    if res == "1":
        hero_name = input("请输入英雄的名称：")
        hero_volume = input("请输入英雄的血量：")
        herr_power = input("请输入英雄的攻击力：")
        hero_info = {"name": hero_name, "volume": hero_volume, "power": herr_power}
        # 字面量插值，f"普通的字符串{变量}"
        print(f"英雄名字为{hero_name}, 英雄血量为{hero_volume}, 英雄攻击力为{herr_power}")
        hero_list.append(hero_info)
    elif res == "2":
        hero_input_name = input("请输入需要查询的英雄信息：")
        # 遍历所有的英雄信息，直到匹配到被查询的英雄
        for i in hero_list:
            # 直到匹配到被查询的英雄
            # if 要查询的英雄信息 == 遍历的每英雄的名字
            if hero_input_name == i['name']:
                print(f"英雄{hero_input_name}的信息为{i}")
    elif res == "3":
        hero_name = input("请输入需要修改的英雄信息：")
        update_hero(hero_list, hero_name)
        print(f"所有英雄信息为{hero_list}")
    elif res == "4":
        hero_delete_name = input("请输入需要删除的英雄信息：")
        delete_hero(hero_list, hero_delete_name)
    else:
        print("退出系统")
        break

print(f"英雄列表中的所有元素为{hero_list}")
