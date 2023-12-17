import pytest

from pythonProject.pytest_practice.game.hero_management import HeroManagement


# 测试类与测试类的定义
# class TestHero3:
#     def test_create_hero_volume_success(self, data):
#         """
#
#         :param volume:
#         :return:
#         """
#         hero_management = HeroManagement()
#         print(f"英雄的血量为{data}")
#         hero_management.create_hero("jinx", data, 20)
#         res = hero_management.find_hero("jinx")
#         assert res.get("name") == "jinx"
#         assert res.get("volume") == data
#
#     def test_create_hero_volume(self, data):
#         print("这是TestHero3类里第二个测试方法")

@pytest.mark.parametrize("volume", [0, 100], ids=["边界值为0", "边界值为100"])
def test_create_hero_fail(volume):
    """

     :param volume:
    :return:
    """
    hero_management = HeroManagement()
    print(f"英雄的血量为{volume}")
    hero_management.create_hero("jinx", volume, 20)
    res = hero_management.find_hero("jinx")
    assert res == False
