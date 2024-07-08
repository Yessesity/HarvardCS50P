from working import convert
import pytest


def test_normal():
    assert convert("12:00 PM to 5:00 PM") == "12:00 to 17:00"
    assert convert("9:00 AM to 6:00 PM") == "09:00 to 18:00"
    assert convert("12:59 PM to 8:00 AM") == "12:59 to 08:00"
    assert convert("3:48 PM to 9:56 AM") == "15:48 to 09:56"


def test_no_minutes():
    assert convert("12 PM to 5 PM") == "12:00 to 17:00"
    assert convert("9 AM to 6 PM") == "09:00 to 18:00"
    assert convert("12 PM to 8 AM") == "12:00 to 08:00"
    assert convert("3 PM to 9 AM") == "15:00 to 09:00"
    assert convert("3:47 PM to 9 AM") == "15:47 to 09:00"
    assert convert("3 PM to 9:47 AM") == "15:00 to 09:47"


def test_hour_or_minute_over_limit():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("09:00 AM - 17:00 PM")


def test_incorrect_format():
    with pytest.raises(ValueError):
        convert("cat")
        convert("3:47 PM - 9:47 AM")
