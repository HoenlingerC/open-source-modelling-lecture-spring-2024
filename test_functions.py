"""This is the test file"""

from functions import add


def test_add():
    assert add(3, 5) == 8
    assert add(6, 1) == 7
    assert add(200, 50) == 250
