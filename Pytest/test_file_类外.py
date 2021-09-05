import pytest


def fun(x):
    return x + 1


def test_A():
    print("test_A")
    assert fun(2) == 3
    # 断言失败


def test_B():
    print("test_B")
    assert fun(2) == 3  # 断言成功


def setup():
    print("打印在（函数）执行之前")


def teardown():
    print("打印在（函数）执行之后")


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_file_类外.py"])
