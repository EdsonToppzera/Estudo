import pytest
from working import convert

def main():
    test_error_convert()
    test_valid_doble_convert()
    test_valid_single_convert()

def test_error_convert():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert(":60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 13:00 PM")

def test_valid_doble_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_valid_single_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

