import pytest
from um import count

def main():
    test_in_words_count()
    test_space_count()
    test_case_count()

def test_in_words_count():
    assert count("um, umbrum") == 1

def test_space_count():
    assert count("um, um ..um..") == 3

def test_case_count():
    assert count("Um, um, UM") == 3
