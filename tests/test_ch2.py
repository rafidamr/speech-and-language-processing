import exercises.ch2 as ch2


def test_2_1():
    assert ch2.method.eval_alphabet("abc")
    assert ch2.method.eval_lower_alphabet("abb")
    assert ch2.method.eval_ab("bababab")


def test_2_2():
    assert ch2.method.eval_repeated_words("the the")
    assert not ch2.method.eval_repeated_words("there here")
    assert ch2.method.eval_lines("12 word\n333aa")
    assert not ch2.method.eval_lines("123\n333")
    assert ch2.method.eval_grotto_raven("asdfgrottossravenasdf")
    assert not ch2.method.eval_grotto_raven("grottos")
    assert ch2.method.eval_first_word("1asdf 'word' asdf a").group() == "word"


def test_2_3():
    el = ch2.ElizaLike()
    assert (
        el.answer("How to grow my business") == "OH SO YOU WANT TO GROW YOUR BUSINESS"
    )
    assert (
        el.answer("What is the best way to sell my properties")
        == "YOU HAVE TO LOOK UP DATA TO SELL YOUR PROPERTIES"
    )
