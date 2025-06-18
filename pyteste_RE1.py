import pytest

def whatever():
    return 9/0

def test_whatever():
    with pytest.raises(ZeroDivisionError):
        whatever()

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_whatever1():
    whatever()