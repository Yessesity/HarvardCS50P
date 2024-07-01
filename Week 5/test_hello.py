from hello1 import hello

def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"


def test_argument_loop():
    for name in ["Harry", "Ron", "Hermione"]:
        assert hello(name) == f"hello, {name}"