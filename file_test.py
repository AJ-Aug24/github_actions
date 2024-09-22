# file_test.py
import pytest

def test_calc_addition():
    # Test the output of 2 + 4
    output = 2 + 4
    assert output == 6

def test_calc_subtraction():
    # Test the output of 2 - 4
    output = 2 - 4
    assert output == -2

def test_calc_multiply():
    # Test the output of 2 * 4
    output = 2 * 4
    assert output == 8

def test_hello():
    # Test if the output returns 'hello'
    output = 'hello'
    assert output == 'hello'
