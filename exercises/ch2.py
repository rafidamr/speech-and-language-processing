import re

#   2.1


def eval_alphabet(s: str) -> re.Match[str] | None:
    "the set of all alphabetic strings"
    return re.findall(r"[a-zA-Z]+", s)


def eval_lower_alphabet(s: str):
    "the set of all lower case alphabetic strings ending in a b"
    return re.findall(r"[a-z]*b", s)


def eval_ab(s: str):
    """
    the set of all strings from the alphabet ab such that each a is
    immediately preceded by and immediately followed by a b
    """
    return re.findall(r"b(ab)+", s)


#   2.2


def eval_repeated_words(s: str):
    """
    the set of all strings with two consecutive repeated words (e.g., “Hum
    bert Humbert” and “the the” but not “the bug” or “the big bug”)
    """
    return re.findall(r"(?:^| )([a-zA-Z]+) \1(?:$| )", s)
