import pytest
from bank import value

def main():
    test_value()


def test_value():
    assert value("Hi") == 20
    assert value("Hello") == 0
    assert value("hello, lil boy") == 0
    assert value("What's up my guy?") == 100
    assert value("I love you!") == 100


if __name__ == "__main__":
    main()
