import pytest

from pythonProject.pytest_practice.game.hero_management import HeroManagement
from pythonProject.pytest_practice.test_game_by_data.load_utits import LoadUitls


@pytest.fixture(params=LoadUitls.load_yaml("volume_data.yaml")["success"])
def get_hero(request):
    new_list = []
    for i in request.param:
        i = i + 1
        new_list.append(i)
    return new_list


# 测试类与测试类的定义
class TestHero:
    # 当血量值设定有效的场景
    def test_create_hero_volume_success(self, get_hero):
        """

        :param volume:
        :return:
        """
        hero_management = HeroManagement()
        print(f"英雄的血量为{get_hero}")
        hero_management.create_hero("jinx", get_hero, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == get_hero

    # 当血量值设定无效的场景， 参数化传入的数据通常为[1, 2, 3, 4](1, 2, 3)
    # 当调用方法的时候。 比如load_yaml()的时候，返回值需要为列表
    @pytest.mark.parametrize("volume", LoadUitls.load_yaml("volume_data.yaml")["fail"])
    def test_create_hero_volume_fail(self, volume):
        """

        :param volume:
        :return:
        """
        hero_management = HeroManagement()
        print(f"英雄的血量为{volume}")
        hero_management.create_hero("jinx", volume, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == volume

    def test_delete_hero(self):
        assert False

    def test_create_hero(self):
        assert False

    def test_find_hero(self):
        assert False

    def test_get_data(self):
        data = LoadUitls.load_yaml("volume_data.yaml")
        print(data)