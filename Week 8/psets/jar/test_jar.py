from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(10)
    assert str(jar) == "🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(2)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(10)
        jar.withdraw(11)