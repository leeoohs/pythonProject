
"""
请输入数字，选择需要完成的操作：1
请输入英雄的名称：jinx
请输入英雄的血量：20
请输入英雄的攻击力：30
创建成功
"""
print("""
1. **创建英雄**
2. **查看英雄信息**
3. **修改英雄信息**
4. **删除英雄**
5. **退出系统**
""")

while True:
    res = input("请输入对应的选项，即可执行对应的操作：")
    if res == "1":
        hero_name = input("请输入英雄的名称：")
        hero_volume = input("请输入英雄的血量：")
        herr_power = input("请输入英雄的攻击力：")
        hero_info = {"name": hero_name, "volume": hero_volume, "power": herr_power}
        # 字面量插值，f"普通的字符串{变量}"
        print(f"英雄名字为{hero_name}, 英雄血量为{hero_volume}, 英雄攻击力为{herr_power}")
    elif res == "2":
        # print(f"查看英雄{hero_info}")
        # 在字符串中，如果用导流引号，符合内单外双，内双外单的规则
        print(f"查看英雄{hero_info['name']}血量为{hero_info['volume']}")
    elif res == "3":
        print("修改英雄信息")
    elif res == "4":
        print("删除英雄")
    else:
        print("退出系统")
        break