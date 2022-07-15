#!/usr/bin/env python3
'''TReich | Alta3 Research
    Using pytest and assert'''

# Define make coffee function with default cups = 1
def make_coffee(cups=1):
    if cups >= 1:
        return f"{cups} cup(s) of coffee coming up!"
    else:
        return None

# Define make decaf with default dc = why bother
def make_decaf(dc="Why bother?"):
    return f"Decaf?! {dc}"

# Define testing functions. Pytest will only recognize functions defined beginning with test_ as tests.
def test_make_coffee():
    assert make_coffee(1) == "1 cup(s) of coffee coming up!"
    assert not make_coffee(0)

# This test will fail!
def test_make_decaf():
    assert make_decaf() == "Decaf?! Sounds great!"
