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

variableType = DFA(
    "variable type",
    'i'+'n'+'t'+'f'+'l'+'o'+'a'+'b'+'e'+'c'+'h'+'r'+'S'+'g',
    table.table["VARIABLE_TYPE"],
    0,
    table.get_final_states("VARIABLE_TYPE"),
)

literalString = DFA(
    "literal string",
    string.digits + string.whitespace + string.ascii_letters + '"',
    table.table["LITERAL_STRING"],
    0,
    table.get_final_states("LITERAL_STRING"),
)

test_public = DFA(
    "public",
    'p' + 'u' + 'b' + 'l' + 'i' + 'c',
    table.table["KEYWORD"],
    0,
    table.get_final_states("KEYWORD"),
)

singleChar.run("'")
singleChar.run("c")
singleChar.run("'")

variableType.run('i')
variableType.run('n')
variableType.run('t')
variableType.reset()
variableType.run('b')
variableType.run('o')
variableType.run('o')
variableType.run('l')
variableType.run('e')
variableType.run('a')
variableType.run('n')

literalString.run('"')
literalString.run('h')
literalString.run('e')
literalString.run('l')
literalString.run('l')
literalString.run('o')
literalString.run(' ')
literalString.run('w')
literalString.run('o')
literalString.run('r')
literalString.run('l')
literalString.run('d')
literalString.run('"')

test_public.run('p')
test_public.run('u')
test_public.run('b')
test_public.run('l')
test_public.run('i')
test_public.run('c')

print(singleChar.isDone())
print(variableType.isDone())
