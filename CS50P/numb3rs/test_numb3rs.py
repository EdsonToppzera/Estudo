import pytest
from numb3rs import validate

def main():
    test_invalid_validate()
    test_valid_validate()

def test_invalid_validate():
    assert validate("cat") == False
    assert validate("230.30.3.10000") == False
    assert validate("255.10.690.100") == False
    assert validate("300") == False
    assert validate("255.69") == False

def test_valid_validate():
    assert validate("185.167.0.1") == True
    assert validate("10.69.0.10") == True
    assert validate("0.0.0.0") == True

if __name__ == "__main__":
    main()
