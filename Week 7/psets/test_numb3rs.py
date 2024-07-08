from numb3rs import validate


def test_random():
    assert validate("255.255.255.255") == True
    assert validate("232.252.101.50") == True
    assert validate("15.66.99.12") == True
    assert validate("60.225.205.148") == True
    assert validate("192.163.135.101") == True


def test_only_first():
    assert validate("111.999.999.999") == False
    assert validate("255.999.999.999") == False


def test_five_byte():
    assert validate("255.255.255.255.255") == False
    assert validate("123.123.123.123.123") == False


def test_too_many_characters():
    assert validate("1.0.0.10000") == False
    assert validate("1.2.3.1000") == False


def test_num_exceed_255():
    assert validate("512.512.512.512") == False
    assert validate("999.999.999.999") == False


def test_words():
    assert validate("cat") == False
    assert validate("dog") == False
    assert validate("Harvard CS50P") == False

