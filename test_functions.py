"""This is the test file"""

from functions import add


def test_add():
    assert add(3, 5) == 8
    assert add(6, 1) == 7
    assert add(200, 50) == 250
    
def test_multiply():
    assert multiply(4,4)== 16
    assert multiply(0,4)== 0
    assert multiply(7,8)== 56