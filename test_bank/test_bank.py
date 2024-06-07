from bank import value

def test_hello():
    assert value("Hello, World") == 0

def test_h_only():
    assert value("Happy 4 you") == 20

def test_no_h_or_hello():
    assert value("World") == 100
