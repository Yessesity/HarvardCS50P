import plates


def test_character_limit():
    assert plates.is_valid("NORMAL") == True
    assert plates.is_valid("WHATISUPDUDES") == False
    assert plates.is_valid("Y") == False


def test_first_two_char_is_letter():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("AAA222") == True


def test_beginning_alphabetical():
    assert plates.is_valid("AA") == True
    assert plates.is_valid("A2") == False
    assert plates.is_valid("2A") == False
    assert plates.is_valid("22") == False
    assert plates.is_valid(" 2") == False


def test_alphanumeric():
    assert plates.is_valid("@#$%^&") == False
    assert plates.is_valid("CS*&%^") == False


def test_punctuation():
    assert plates.is_valid("NORMAL") == True
    assert plates.is_valid("N.OR,") == False


def test_letter_inbetween_number():
    assert plates.is_valid("BB55P6") ==  False
    assert plates.is_valid("CS5P0") == False


def test_number_inbetween_letter():
    assert plates.is_valid("CS50P") == False
    assert plates.is_valid("AAA22A") == False


def test_first_num_0():
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("BO0313") == False
