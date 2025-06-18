# coding=utf-8
import pytest


def whatever():
    return 9/0

def test_whatever():
    try:
        whatever()
    except ZeroDivisionError as exc:
        pytest.fail(exc, pytrace=True)