import pytest
from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("BARONE") == "BRN"
    assert shorten("AOA") == ""
    assert shorten("barone") == "brn"
    assert shorten("B4RON3") == "B4RN3"
    assert shorten("BARONE!?") == "BRN!?"

if __name__ == "__main__":
    main()
