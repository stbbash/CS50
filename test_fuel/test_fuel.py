from fuel import convert, gauge
import pytest


def test_gauge_percent():
    assert gauge(25) == "25%"

def test_gauge_lower():
    assert gauge(1) == "E"

def test_gauge_greater():
    assert gauge(99) == "F"

def test_convert():
    assert convert("20/80") == 25

def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    with pytest.raises(ValueError):
        convert("50/10")
