# -*- coding: utf-8 -*-
import string


class TransitionTable:
    def __init__(self):
        self.SINGLE_CHARACTER = {
            0: {"'": 1},
            1: {string.ascii_letters: 3, string.digits: 2, " ": 4},
            2: {"'": 5},
            3: {"'": 5},
            4: {"'": 5},
            5: "done",
        }
