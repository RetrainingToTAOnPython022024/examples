import pytest
from src.app import div


def test_app_1():
    print(__name__)
    assert 3 ==  div(9, 3)


def test_app_2():
    assert 4 ==  div(9, 3)
