from plates import is_valid

def test_is_valid():
    assert is_valid("aa12") == True

def test_first_two_letter_alpha():
    assert is_valid("aa0") == False

def test_alpha_after_number():
    assert is_valid("aa2a") == False

def test_start_with_number():
    assert is_valid("2222") == False

def test_length():
    assert is_valid("aa222222") == False

def test_alpah_numeric():
    assert is_valid("aa!$") == False

def test_empty():
    assert is_valid("") == False
