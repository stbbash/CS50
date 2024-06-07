from twttr import shorten

def test_shorten():
    assert shorten("Hello, World") == "Hll, Wrld"

def test_capital():
    assert shorten("HELLO") == "HLL"

def test_numbers():
    assert shorten("12345") == "12345"

