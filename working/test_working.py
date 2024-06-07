from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

    with pytest.raises(ValueError):
        convert("10 PM 8 AM")

    with pytest.raises(ValueError):
        convert("13 PM to 8 AM")

