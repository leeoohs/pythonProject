import pytest


@pytest.fixture(params=[0, 1])
def a(request):
    return request.param


def test_a(a):
    print(a)