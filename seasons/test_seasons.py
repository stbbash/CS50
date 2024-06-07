from seasons import calculate_age_in_minutes

def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes("2023-02-09") == "Five hundred twenty-five thousand, six hundred minutes"
    assert calculate_age_in_minutes("2022-02-09") == "One million, fifty-one thousand, two hundred minutes"
