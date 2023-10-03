def summator(a, b):
    return a + b

def test_one():
    assert summator(10, 20) == 30

def test_two():
    assert summator(-10, -7) == 20
