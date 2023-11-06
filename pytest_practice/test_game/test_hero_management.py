# 实例化类 类名()
from pythonProject.pytest_practice.game.hero_management import HeroManagement

hero_management = HeroManagement()


def setup():
    hero_management.create_hero("jinx", 20, 20)


def test_create_hero():
    """
    1.创建英雄。
    2.断言查询英雄是否创建成功
        查询英雄，如果存在，就认为创建成功
    :return:
    """
    # 测试步骤
    res = hero_management.find_hero("jinx")
    # print(res)
    # 如果不为None 也不为False 就当成Ture 进行处理，则为通过
    assert res
    # 确定创建的英雄的数据是正确的
    assert res.get("name") == "jinx"
    assert res.get("volume") == 20
    assert res.get("power") == 20


def test_find_hero():
    res = hero_management.find_hero("jinx")
    res2 = hero_management.find_hero("ez")
    assert res.get("name") == "jinx"
    assert res2 == False


def test_update_hero():
    hero_management.update_hero("jinx", 22)
    res = hero_management.find_hero("jinx")
    assert res.get("volume") == 22


def test_delete_hero():
    hero_management.delete_hero("jinx")
    res = hero_management.find_hero("jinx")
    assert res == False



