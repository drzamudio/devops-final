from app import add, multiply

def test_add():
    assert add(1, 1) == 2
    assert add(0, 5) == 5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0
