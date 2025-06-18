def whatever():
    return 9/0

try:
    whatever()
    assert False
except TypeError:
    assert True