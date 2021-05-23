# -*- coding: utf-8 -*-
from transtable import TransitionTable
from dfa import DFA
import string, sys


table = TransitionTable()
# Create DFAs in list of tokens consisting of
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ single character, variable type, literal string              ┃
# ┃ signed integer, boolean string, white space                  ┃
# ┃ arithmetic operator, assignment operator, comparison operator┃
# ┃ terminating symbol, different types of parentheses           ┃
# ┃ comma, identifier, keyword                                   ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
singleChar = DFA(
    "SINGLE CHARACTER",
    string.digits + string.ascii_letters + "'" + " ",
    table.table["SINGLE_CHARACTER"],
    0,
    table.get_final_states("SINGLE_CHARACTER"),
)

variableType = DFA(
    "VARIABLE TYPE",
    "i" + "n" + "t" + "f" + "l" + "o" + "a" + "b" + "e" + "c" + "h" + "r" + "S" + "g",
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
    string.digits + "-",
    table.table["SIGNED_INTEGER"],
    0,
    table.get_final_states("SIGNED_INTEGER"),
)

booleanString = DFA(
    "BOOLEAN STRING",
    "t" + "r" + "u" + "e" + "f" + "a" + "l" + "s",
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
    "+" + "-" + "/" + "*",
    table.table["ARITHMETIC_OPERATOR"],
    0,
    table.get_final_states("ARITHMETIC_OPERATOR"),
)

assignmentOperator = DFA(
    "ASSIGNMENT OPERATOR",
    "=",
    table.table["ASSIGNMENT_OPERATOR"],
    0,
    table.get_final_states("ASSIGNMENT_OPERATOR"),
)

comparisonOperator = DFA(
    "COMPARISON OPERATOR",
    "<" + ">" + "=" + "!",
    table.table["COMPARISON_OPERATOR"],
    0,
    table.get_final_states("COMPARISON_OPERATOR"),
)

terminatingSymbol = DFA(
    "TERMINATING SYMBOL",
    ";",
    table.table["TERMINATING_SYMBOL"],
    0,
    table.get_final_states("TERMINATING_SYMBOL"),
)

lparen = DFA(
    "LPAREN",
    "(",
    table.table["LPAREN"],
    0,
    table.get_final_states("LPAREN"),
)

rparen = DFA(
    "RPAREN",
    ")",
    table.table["RPAREN"],
    0,
    table.get_final_states("RPAREN"),
)

lbrace = DFA(
    "LBRACE",
    "{",
    table.table["LBRACE"],
    0,
    table.get_final_states("LBRACE"),
)

rbrace = DFA(
    "RBRACE",
    "}",
    table.table["RBRACE"],
    0,
    table.get_final_states("RBRACE"),
)

lbranket = DFA(
    "LBRANKET",
    "[",
    table.table["LBRANKET"],
    0,
    table.get_final_states("LBRANKET"),
)

rbranket = DFA(
    "RBRANKET",
    "]",
    table.table["RBRANKET"],
    0,
    table.get_final_states("RBRANKET"),
)

comma = DFA(
    "COMMA",
    ",",
    table.table["COMMA"],
    0,
    table.get_final_states("COMMA"),
)

identifier = DFA(
    "IDENTIFIER",
    "_" + string.digits + string.ascii_letters,
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
# lexical analyzer is a list of DFAs
# and the order is the weight of the DFA(the higher it is in the front)
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
output = []
# list of pass dfa : appended when dfa reached final state
getReady = []
if len(sys.argv) != 1:
    f = open(sys.argv[1], "r")
else:
    f = open("test.java", "r")
value = ""
#           -*-    How to lexical analyzer works    -*-
# 1. Open the file
# 2. perform DFA one by one letter until eof.
#   2-1. if DFA in 'getReady' got illegal input, goto 4.
#   2-2. if DFA reached final state, put in 'getReady'
# 3. 'input' concatenate to 'value', repeat the procedure 2.
# 4. puts token and 'value' on 'output', reset all DFA and clear 'getReady'
# 5. perform DFA via current input and check 2-2. goto 2.
for input in f.read():
    # to check earn output
    flag = False
    for dfa in lexical_analyzer:
        success = dfa.run(input)
        if not success and dfa in getReady:
            # basically '-' is recognized as an arithmetic operator
            # if <SIGNED INTEGER> follows the '-', the previous token is determine whether '-' in number or operator
            if len(output) > 0:
                if (
                    dfa.name == "SIGNED INTEGER"
                    and output[-1][0] == "<ARITHMETIC OPERATOR>"
                ) and output[-1][1] == "-":
                    if len(output) > 1:
                        # ignore <WHITE SPACE>
                        if output[-2][0] == "<WHITE SPACE>":
                            idx = -3
                        else:
                            idx = -2
                        if (
                            output[idx][0] == "<ASSIGNMENT OPERATOR>"
                            or output[idx][0] == "<ARITHMETIC OPERATOR>"
                            or output[idx][0] == "<COMMA>"
                            or output[idx][0] == "<LPAREN>"
                        ):
                            output.pop()
                            value = "-" + value
            # skip ASSIGNMENT OPERATOR when input value is '=' to recognize '=='
            if dfa.name == "ASSIGNMENT OPERATOR" and input == "=":
                continue
            # skip KEYWORD when input value is in alphabet in IDENTIFIER
            elif (
                dfa.name == "KEYWORD"
                and input in string.digits + string.ascii_letters + "_"
            ):
                getReady.remove(dfa)
                continue
            output.append(("<" + dfa.name + ">", value))
            value = ""
            getReady.clear()
            # earn output
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

isError = False
# last value handling
if getReady:
    output.append(("<" + getReady.pop().name + ">", value))
else:
    isError = True
    print("Error occurred at input:\n", value, "\nOutput below is analyze result until error occurred.")

# error handling when negative integer comes to eof
# <operator, '-'>, <signed integer, '123'> => <signed integer, '-123'>

if len(output) == 2:
    if (
        output[-1][0] == "<SIGNED INTEGER>"
        and output[-1][1] != "0"
        and output[-2][1] == "-"
    ):
        v = output.pop()[1]
        output.pop()
        output.append(("<SIGNED INTEGER>", "-" + v))
elif len(output) > 2:
    if (
            output[-1][0] == "<SIGNED INTEGER>"
            and output[-2][1] == "-"
            and output[-3][1] == "-"
    ):
        v = output.pop()[1]
        output.pop()
        output.append(("<SIGNED INTEGER>", "-" + v))

f.close()
# write file output
if len(sys.argv) != 1:
    f = open(sys.argv[1].split(".")[0] + "_output.txt", "w")
else:
    f = open("output.txt", "w")
if isError:
    f.write("Error occurred at input:\n" + value + "\nOutput below is analyze result until error occurred.\n")
for token, v in output:
    # skip white space
    if token == "<WHITE SPACE>":
        continue
    f.write(token + " " + v + "\n")
    print(token, v)
f.close()
