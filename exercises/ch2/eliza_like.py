import re


class ElizaLike:
    """
    A business consultant program that behaves like Eliza
    """

    def __init__(self):
        "list of tuples for patterns and their templates"
        self.TUPLES = [
            (re.compile(r".*HOW TO\s+(.*)"), r"OH SO YOU WANT TO \1"),
            (
                re.compile(r".*WHAT IS THE BEST\s+.*\s+TO\s+(.*)"),
                r"YOU HAVE TO LOOK UP DATA TO \1",
            ),
        ]
        self.COMMONS = [
            (re.compile(r"(.*) MY (.*)"), r"\1 YOUR \2"),
        ]

    def answer(self, s: str):
        s, out = s.upper(), None
        for pattern, template in self.COMMONS:
            if pattern.search(s):
                s = pattern.sub(template, s)
        for pattern, template in self.TUPLES:
            if pattern.search(s):
                out = pattern.sub(template, s)
                break
        return out
