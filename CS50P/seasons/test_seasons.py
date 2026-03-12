import pytest
from datetime import date
from seasons import Count, get_minutagem

def main():
    test_count_initialization()
    test_count_invalid_date()

def test_count_initialization():
    assert Count("2020-12-20").data == "2020-12-20"

def test_count_invalid_date():
    try:
        Count("invalid-date").conta()
        assert False, "Expected sys.exit to be called with 'Invalid date'"
    except SystemExit as e:
        assert str(e) == "Invalid date"

if __name__ == "__main__":
    pytest.main()
