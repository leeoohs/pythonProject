import pytest


@pytest.mark.run(order=1)
def test_one():
    print("test1")

@pytest.mark.run(order=3)
def test_two():
    print("test2")

@pytest.mark.run(order=2)
def test_three():
    print("test3")

@pytest.mark.run(order=4)
def test_four():
    print("test4")