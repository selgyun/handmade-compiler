# -*- coding: utf-8 -*-

from transtable import TransitionTable
from dfa import DFA
import string


table = TransitionTable()
singleChar = DFA(
    "SINGLE CHARACTER",
    string.digits + string.ascii_letters + "'" + " ",
    table.table["SINGLE_CHARACTER"],
    0,
    table.get_final_states("SINGLE_CHARACTER"),
)

variableType = DFA(
    "VARIABLE TYPE",
    'i'+'n'+'t'+'f'+'l'+'o'+'a'+'b'+'e'+'c'+'h'+'r'+'S'+'g',
    table.table["VARIABLE_TYPE"],
    0,
    table.get_final_states("VARIABLE_TYPE"),
)

literalString = DFA(
    "LITERAL STRING",
    string.digits + string.whitespace + string.ascii_letters + '"',
    table.table["LITERAL_STRING"],
    0,
    table.get_final_states("LITERAL_STRING"),
)

signedInteger = DFA(
    "SIGNED INTEGER",
    string.digits + '-',
    table.table["SIGNED_INTEGER"],
    0,
    table.get_final_states("SIGNED_INTEGER"),
)

booleanString = DFA(
    "BOOLEAN STRING",
    't' + 'r' + 'u' + 'e' + 'f' + 'a' + 'l' + 's',
    table.table["BOOLEAN_STRING"],
    0,
    table.get_final_states("BOOLEAN_STRING"),
)

whiteSpace = DFA(
    "WHITE SPACE",
    string.whitespace,
    table.table["WHITE_SPACE"],
    0,
    table.get_final_states("WHITE_SPACE"),
)

arithmeticOperator = DFA(
    "ARITHMETIC OPERATOR",
    '+' + '-' + '/' + '*',
    table.table["ARITHMETIC_OPERATOR"],
    0,
    table.get_final_states("ARITHMETIC_OPERATOR"),
)

assignmentOperator = DFA(
    "ASSIGNMENT OPERATOR",
    '=',
    table.table["ASSIGNMENT_OPERATOR"],
    0,
    table.get_final_states("ASSIGNMENT_OPERATOR"),
)

comparisonOperator = DFA(
    "COMPARISON OPERATOR",
    '<' + '>' + '=' +'!',
    table.table["COMPARISON_OPERATOR"],
    0,
    table.get_final_states("COMPARISON_OPERATOR"),
)

terminatingSymbol = DFA(
    "TERMINATING SYMBOL",
    ';',
    table.table["TERMINATING_SYMBOL"],
    0,
    table.get_final_states("TERMINATING_SYMBOL"),
)

lparen = DFA(
    "LPAREN",
    '(',
    table.table["LPAREN"],
    0,
    table.get_final_states("LPAREN"),
)

rparen = DFA(
    "RPAREN",
    ')',
    table.table["RPAREN"],
    0,
    table.get_final_states("RPAREN"),
)

lbrace = DFA(
    "LBRACE",
    '{',
    table.table["LBRACE"],
    0,
    table.get_final_states("LBRACE"),
)

rbrace = DFA(
    "RBRACE",
    '}',
    table.table["RBRACE"],
    0,
    table.get_final_states("RBRACE"),
)

lbranket = DFA(
    "LBRANKET",
    '[',
    table.table["LBRANKET"],
    0,
    table.get_final_states("LBRANKET"),
)

rbranket = DFA(
    "RBRANKET",
    ']',
    table.table["RBRANKET"],
    0,
    table.get_final_states("RBRANKET"),
)

comma = DFA(
    "COMMA",
    ',',
    table.table["COMMA"],
    0,
    table.get_final_states("COMMA"),
)

identifier = DFA(
    "IDENTIFIER",
    '_' + string.digits + string.ascii_letters,
    table.table["IDENTIFIER"],
    0,
    table.get_final_states("IDENTIFIER"),
)

keyword = DFA(
    "KEYWORD",
    string.ascii_letters,
    table.table["KEYWORD"],
    0,
    table.get_final_states("KEYWORD"),
)

lexical_analyzer = [
    keyword,
    singleChar,
    variableType,
    signedInteger,
    literalString,
    booleanString,
    whiteSpace,
    arithmeticOperator,
    comparisonOperator,
    assignmentOperator,
    terminatingSymbol,
    lparen,
    rparen,
    lbrace,
    rbrace,
    lbranket,
    rbranket,
    comma,
    identifier,
]
# output of lexical analyzer
# list of pass dfa
output = []
getReady = []
f = open("test.java", 'r')
value = ""
# How to lexical analyzer works
# 1. Open the file and perform DFA one letter at a time.
# 2. Confirm that the DFA has been passed by receiving the following letters for the passed DFA
# 3. if DFA is passed, perform 1. again for the current input value
for input in f.read():
    # to check earn output
    flag = False
    for dfa in lexical_analyzer:
        success = dfa.run(input)
        if not success and dfa in getReady:
            # if <SIGNED INTEGER> follows the '-', the previous token is determine whether '-' in number or operator
            if len(output) > 0:
                if (dfa.name == "SIGNED INTEGER" and output[-1][0] == "<ARITHMETIC OPERATOR>") and output[-1][1] == '-':
                    if len(output) > 1:
                        if output[-2][0] == "<WHITE SPACE>":
                            idx = -3
                        else:
                            idx = -2
                        if output[idx][0] == "<ASSIGNMENT OPERATOR>" or output[idx][0] == "<ARITHMETIC OPERATOR>":
                            output.pop()
                            value = '-' + value
            if dfa.name == "ASSIGNMENT OPERATOR" and input == "=":
                continue
            elif dfa.name == "KEYWORD" and input in string.digits + string.ascii_letters + '_':
                getReady.remove(dfa)
                continue
            output.append(("<" + dfa.name + ">", value))
            value = ""
            getReady.clear()
            flag = True
            for reset_dfa in lexical_analyzer:
                reset_dfa.reset()
            break
        if dfa.isDone() and dfa not in getReady:
            getReady.append(dfa)
    if flag:
        for dfa in lexical_analyzer:
            dfa.run(input)
            if dfa.isDone():
                getReady.append(dfa)
    value += input
if getReady:
    output.append(("<" + getReady.pop().name + ">", value))
else:
    print(value, 'occurred error')

if len(output) > 1:
    if output[-1][0] == "<SIGNED INTEGER>" and output[-2][1] == '-':
        v = output.pop()[1]
        output.pop()
        output.append(("<SIGNED INTEGER>", '-' + v))

f.close()
f = open("output.txt", 'w')
for token, v in output:
    if token == "<WHITE SPACE>":
        continue
    f.write(token + " " + v + "\n")
    print(token, v)
f.close()

