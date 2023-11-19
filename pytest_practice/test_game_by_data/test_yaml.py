# 读取yaml文件信息
import pytest
import yaml

from pythonProject.pytest_practice.test_game_by_data.load_utits import LoadUitls


def test_yaml():
    # open("文件名") 打开文件
    # yaml.safe_load 把yaml文件中的数据转换成Python 可以理解的数据信息
    data = yaml.safe_load(open("yaml_demo.yaml"))
    print(data)

#
# @pytest.mark.parametrize("data", [1,2,3])
# def test_loas_data(data):
#     assert data == 1


@pytest.mark.parametrize("data", LoadUitls.load_yaml("hp_data.yaml"))
def test_load_data(data):
    assert data == 1