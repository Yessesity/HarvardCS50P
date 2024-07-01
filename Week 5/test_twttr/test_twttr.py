from twttr import shorten

def test_shorten_standard():
    assert shorten("Hello my man") == "Hll my mn"
    assert shorten("What's up") == "Wht's p"

def test_shorten_punctuation():
    assert shorten("Hi, how are ya?") == "H, hw r y?"
    assert shorten("Hello, world.") == "Hll, wrld."


def test_shorten_numbers():
    assert shorten("123") == "123"
    assert shorten("456") == "456"


def test_shorten_all_cases():
    assert shorten("EYO") == "Y"
    assert shorten("eyo") == "y"
