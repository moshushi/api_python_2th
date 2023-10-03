import pytest

from src.summator import summator


# from ../src/summator import summator
# from summator import summator

def test_one():
    assert summator(10, 20) == 30


@pytest.mark.smoke
def test_two():
    #    assert summator(-10, -7) == 20
    assert summator(-10, -7) == -17
