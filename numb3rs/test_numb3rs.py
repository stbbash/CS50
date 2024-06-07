from numb3rs import validate
import pytest
def test_validate():
    assert validate("276.0.0.0.") == False
    assert validate("255.0.0.0") == True
    assert validate("255") == False
    assert validate("0.0.127.1") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.2.3.4") == True
    assert validate("128.2.3.4") == True
    assert validate("cat") == False
