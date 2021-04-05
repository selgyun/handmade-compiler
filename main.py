# -*- coding: utf-8 -*-

from transtable import TransitionTable
from dfa import DFA
import string

table = TransitionTable()
# print(table.table)
singleChar = DFA(
    "single character",
    string.digits + string.ascii_letters + "'",
    table.table["SINGLE_CHARACTER"],
    0,
    table.get_final_states("SINGLE_CHARACTER"),
)

singleChar.run("'")
singleChar.run("c")
singleChar.run("'")

print(singleChar.isDone())
