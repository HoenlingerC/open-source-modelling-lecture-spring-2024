"""This is the test file"""

from functions import add
from functions import multiply


def test_add():
    assert add(3, 5) == 8
    assert add(6, 1) == 7
    assert add(200, 50) == 250
    

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(6, 1) == 6
    assert multiply(200, 50) == 10000
    assert multiply(0, 50) == 0
