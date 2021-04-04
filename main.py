# -*- coding: utf-8 -*-

from transtable import TransitionTable
from dfa import DFA
import string

table = TransitionTable()
# print(table.SINGLE_CHARACTER)
singleChar = DFA(
    "single character",
    string.digits + string.ascii_letters + "'",
    table.SINGLE_CHARACTER,
    0,
    5,
)

singleChar.run("'")
singleChar.run("c")
singleChar.run("'")

print(singleChar.isDone())
