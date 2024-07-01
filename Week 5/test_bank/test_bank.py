from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("hello, hi there!") == 0
    assert value("HELLO, hi there!") == 0


def test_value_h():
    assert value("h") == 20
    assert value("hey dude") == 20
    assert value("HEYAAAAAAAA MANNNN") == 20


def test_value_otherwise():
    assert value("123") == 100
    assert value("what?") == 100
    assert value("nefNJJFEefF-13I") == 100
