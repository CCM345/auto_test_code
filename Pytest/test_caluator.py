# -*- coding: UTF-8 -*-
"""
功能：
作者：
时间：
修改记录：
"""
import os
import pytest
from Pytest.caluator import add, sub, mul, div, remiander

X = 10
Y = 20


def test_add():
    assert add(X, Y) == 30


def test_sub():
    assert sub(X, Y) == -10


def test_mul():
    assert mul(X, Y) == 200


def test_div():
    assert div(X, Y) == 0.5


def test_reminder():
    assert remiander(X, Y) == 10


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_caluator.py", "--alluredir", "./allure-results"])
    os.system("allure generate ./allure-results -o ./reports")
