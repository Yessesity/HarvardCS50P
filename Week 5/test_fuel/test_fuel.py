import fuel
import pytest


def test_normal_int():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("2/3") == 67


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("2/0")

def test_value_error_string():
    with pytest.raises(ValueError):
        fuel.convert("cat")
        fuel.convert("three/fourths")


def test_value_error_x_bigger_than_y():
    with pytest.raises(ValueError):
        fuel.convert("10/3")


def test_gauge_empty():
    assert fuel.gauge(1) == "E"


def test_gauge_full():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"


def test_gauge_print():
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(67) == "67%"
