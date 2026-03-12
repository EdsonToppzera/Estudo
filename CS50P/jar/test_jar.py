from jar import Jar


def test_init():
    jar = Jar()
    jar.capacity == -1
    assert ValueError

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    size = jar.size
    assert size == 1


def test_withdraw():
    jar = Jar()
    try:
        jar.withdraw(1)
    except ValueError:
        pass
    else:
        assert False
