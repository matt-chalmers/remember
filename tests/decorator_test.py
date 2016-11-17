
from remember.decorator import remember


def test_brackets():

    @remember()
    def testf():
        return 42

    assert testf() == 42


def test_nobrackets():

    @remember
    def testf():
        return 42

    assert testf() == 42
