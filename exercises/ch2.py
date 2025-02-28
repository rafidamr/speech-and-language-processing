import re


def eval_alphabet(s: str):
    "the set of all alphabetic strings"
    return re.fullmatch("^[a-zA-Z]+", s)


def eval_lower_alphabet(s: str):
    """
    the set of all strings from the alphabet ab such that each a
    is immediately preceded by and immediately followed by a b
    """
    return re.fullmatch("^[a-z]+b$", s)


def eval_ab(s: str):
    """
    the set of all strings from the alphabet ab such that each a is immedi
    ately preceded by and immediately followed by a b;
    """
    return re.fullmatch("^b(ab)+", s)
