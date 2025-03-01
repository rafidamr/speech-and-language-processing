from exercises import *


def test_2_1():
    assert ch2.eval_alphabet("abc")
    assert ch2.eval_lower_alphabet("abb")
    assert ch2.eval_ab("bababab")


def test_2_2():
    assert ch2.eval_repeated_words("the the")
    assert not ch2.eval_repeated_words("there here")
