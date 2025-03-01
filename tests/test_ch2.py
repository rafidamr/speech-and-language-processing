from exercises import *


def test_2_1():
    assert ch2.eval_alphabet("abc")
    assert ch2.eval_lower_alphabet("abb")
    assert ch2.eval_ab("bababab")


def test_2_2():
    assert ch2.eval_repeated_words("the the")
    assert not ch2.eval_repeated_words("there here")
    assert ch2.eval_lines("12 word\n333aa")
    assert not ch2.eval_lines("123\n333")
    assert ch2.eval_grotto_raven("asdfgrottossravenasdf")
    assert not ch2.eval_grotto_raven("grottos")
    assert ch2.eval_first_word("1asdf 'word' asdf a").group() == "word"
