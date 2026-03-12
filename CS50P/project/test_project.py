from project import validate_language, validate_currency, validate_price

def test_validate_language():
    assert validate_language("en") == "ok"
    assert validate_language("pt") == "ok"
    assert validate_language("asd") == "not ok"

def test_validate_currency():
    assert validate_currency("BRL") == "ok"
    assert validate_currency("CAD") == "ok"
    assert validate_currency("asd") == "not ok"

def test_validate_price():
    assert validate_price("10") == "ok"
    assert validate_price("0.1") == "ok"
    assert validate_price("ten") == "not ok"
