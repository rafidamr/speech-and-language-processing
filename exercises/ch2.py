import re

def eval_alphabet(s: str):
    return re.fullmatch('^[a-zA-Z]+', s)

def eval_lower_alphabet(s: str):
    return re.fullmatch('^[a-z]+b$', s)