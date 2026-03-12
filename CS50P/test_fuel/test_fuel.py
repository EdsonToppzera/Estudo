import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_erros()

def test_convert():
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("5/10") == 50 and gauge(50) == "50%"

def test_erros():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("11/10")


if __name__ == "__main__":
    main()
