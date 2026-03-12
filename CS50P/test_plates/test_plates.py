import pytest
from plates import is_valid

def main():
    test_is_valid()

def test_is_valid():
    assert is_valid("GOZA5") == True
    assert is_valid("FOD3") == True
    assert is_valid("SLAK96") == True
    assert is_valid("96LOKO") == False
    assert is_valid("EUQUEROGOZAPORRAEUAMOGOZA") == False
    assert is_valid("SLA6O9") == False
    assert is_valid("SLA000") == False
    assert is_valid("SLA96*") == False
    assert is_valid("531005") == False

if __name__ == "__main__":
    main()

