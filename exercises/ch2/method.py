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
    return re.findall(r"b(?:ab)+", s)


#   2.2


def eval_repeated_words(s: str):
    """
    the set of all strings with two consecutive repeated words (e.g., “Hum
    bert Humbert” and “the the” but not “the bug” or “the big bug”)
    """
    return re.findall(r"(?:^|\s)(\w+) \1(?:$|\s)", s)


def eval_lines(s: str):
    """
    all strings that start at the beginning of the line with an integer and that
    end at the end of the line with a word
    """
    return re.findall(r"^\d+.*[a-zA-Z]+$", s, flags=re.MULTILINE)


def eval_grotto_raven(s: str):
    """
    all strings that have both the word grotto and the word raven in them
    (but not, e.g., words like grottos that merely contain the word grotto)
    """
    return re.findall(r".*(?:raven|grotto).*(?:grotto|raven).*", s)


def eval_first_word(s: str):
    """
    write a pattern that places the first word of an English sentence in a
    register. Deal with punctuation.
    """
    return re.search(r"\b([a-zA-Z]+)\b", s)
