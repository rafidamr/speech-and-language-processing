import re


class ElizaLike:
    "A simple consultant program that behaves like Eliza of Weizenbaum (1966)"

    def __init__(self):
        "list of question patterns and their answer templates"
        self.ANSWERS = [
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
        for pattern, template in self.ANSWERS:
            if pattern.search(s):
                out = pattern.sub(template, s)
                break
        return out
