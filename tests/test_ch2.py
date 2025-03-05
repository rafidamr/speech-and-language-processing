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


def test_2_4():
    med = ch2.MinimumEditDistance("leda", "deal", s_cost=1)
    assert (
        med.get_grid()
        == r"   #  d  e  a  l  \n#  0  1  2  3  4  \nl  1  1  2  3  3  \ne  2  2  1  2  3  \nd  3  2  2  2  3  \na  4  3  3  2  3  \n"
    )


def test_2_5():
    med1 = ch2.MinimumEditDistance("drive", "brief", s_cost=1)
    med2 = ch2.MinimumEditDistance("drive", "divers", s_cost=1)
    assert med1.get_distance() == med2.get_distance()
    med1 = ch2.MinimumEditDistance("drive", "brief", s_cost=2)
    med2 = ch2.MinimumEditDistance("drive", "divers", s_cost=2)
    assert med1.get_distance() > med2.get_distance()


def test_2_6__2_7():
    med = ch2.MinimumEditDistanceAndAlignment("INTENTION", "EXECUTION", s_cost=2)
    assert (
        med.get_alignment()
        == r"I * <- delete\nN E <- substitute\nT X <- substitute\nE E\n* C <- insert\nN U <- substitute\nT T\nI I\nO O\nN N\n"
    )
