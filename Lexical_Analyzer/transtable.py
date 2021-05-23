# -*- coding: utf-8 -*-
import string


# build_transition_table_with_lexemes build transition table
# very easily from lexemes.
# You can pass lexemes of the rule.
# Note that this function works only when lexemes' first letter is
# all different. If not, it won't be DFA transition rule.
# e.g. build_transition_table_with_lexemes(["if", "else", "while"])
def build_transition_table_with_lexemes(lexemes):
    transition_table = {}
    i = 0
    final_state = 1
    for lexeme in lexemes:
        final_state += len(lexeme) - 1

    transition_table["final"] = [final_state]
    transition_table[final_state] = {}

    for lexeme in lexemes:
        for j, c in enumerate(lexeme):
            if j == 0:
                if i == 0:
                    transition_table[0] = {c: i + j + 1}
                    continue
                transition_table[0] = {**transition_table[0], c: i + j + 1}
                continue

            if j + 1 == len(lexeme) and final_state != 0:
                transition_table[i + j] = {c: final_state}
                i += j
                continue

            transition_table[i + j] = {c: i + j + 1}

    return transition_table


# Define the transition table to this class
class TransitionTable:
    def __init__(self):
        # Transition table is represented with
        # "Transition Name": {
        #   <state> : {
        #     "transition key" : <next state>
        #   }
        # }
        self.table = {
            "SINGLE_CHARACTER": {
                0: {"'": 1},
                1: {
                    string.ascii_letters: 3,
                    string.digits: 2,
                    " ": 4,
                },
                2: {"'": 5},
                3: {"'": 5},
                4: {"'": 5},
                5: {},
                "final": [5],
            },
            # int, char, boolean, String
            "VARIABLE_TYPE": {
                0: {"i": 1, "c": 3, "b": 6, "S": 12},
                1: {"n": 2},
                2: {"t": 17},
                3: {"h": 4},
                4: {"a": 5},
                5: {"r": 17},
                6: {"o": 7},
                7: {"o": 8},
                8: {"l": 9},
                9: {"e": 10},
                10: {"a": 11},
                11: {"n": 17},
                12: {"t": 13},
                13: {"r": 14},
                14: {"i": 15},
                15: {"n": 16},
                16: {"g": 17},
                17: {},
                "final": [17],
            },
            "SIGNED_INTEGER": {
                0: {"0": 3, "-": 1, string.digits.replace("0", ""): 2},
                1: {string.digits.replace("0", ""): 2},
                2: {string.digits: 2},
                3: {},
                "final": [2, 3],
            },
            # true, false
            "BOOLEAN_STRING": {
                0: {"t": 1, "f": 3},
                1: {"r": 2},
                2: {"u": 6},
                3: {"a": 4},
                4: {"l": 5},
                5: {"s": 6},
                6: {"e": 7},
                7: {},
                "final": [7],
            },
            "WHITE_SPACE": {
                0: {string.whitespace: 1},
                1: {string.whitespace: 1},
                "final": [1],
            },
            "ARITHMETIC_OPERATOR": {
                0: {"+": 1, "*": 1, "-": 1, "/": 1},
                1: {},
                "final": [1],
            },
            "ASSIGNMENT_OPERATOR": {
                0: {"=": 1},
                1: {},
                "final": [1],
            },
            "COMPARISON_OPERATOR": {
                0: {"<": 1, ">": 1, "=": 2, "!": 2},
                1: {"=": 3},
                2: {"=": 3},
                3: {},
                "final": [1, 3],
            },
            "TERMINATING_SYMBOL": {
                0: {";": 1},
                1: {},
                "final": [1],
            },
            "LPAREN": {
                0: {"(": 1},
                1: {},
                "final": [1],
            },
            "RPAREN": {
                0: {")": 1},
                1: {},
                "final": [1],
            },
            "LBRACE": {
                0: {"{": 1},
                1: {},
                "final": [1],
            },
            "RBRACE": {
                0: {"}": 1},
                1: {},
                "final": [1],
            },
            "LBRANKET": {
                0: {"[": 1},
                1: {},
                "final": [1],
            },
            "RBRANKET": {
                0: {"]": 1},
                1: {},
                "final": [1],
            },
            "COMMA": {
                0: {",": 1},
                1: {},
                "final": [1],
            },
            "LITERAL_STRING": {
                0: {'"': 1},
                1: {
                    string.ascii_letters: 2,
                    string.digits: 3,
                    string.whitespace: 4,
                    '"': 5,
                },
                2: {
                    string.ascii_letters: 3,
                    string.digits: 4,
                    string.whitespace: 1,
                    '"': 5,
                },
                3: {
                    string.ascii_letters: 4,
                    string.digits: 1,
                    string.whitespace: 2,
                    '"': 5,
                },
                4: {
                    string.ascii_letters: 1,
                    string.digits: 2,
                    string.whitespace: 3,
                    '"': 5,
                },
                5: {},
                "final": [5],
            },
            "IDENTIFIER": {
                0: {"_": 1, string.ascii_letters: 2},
                1: {string.ascii_letters: 2, string.digits: 3, "_": 1},
                2: {string.ascii_letters: 3, string.digits: 1, "_": 2},
                3: {string.ascii_letters: 1, string.digits: 2, "_": 3},
                "final": [1, 2, 3],
            },
        }

        self.table["KEYWORD"] = build_transition_table_with_lexemes(
            [
                "if",
                "else",
                "while",
                "class",
                "return",
                "public",
                "main",
                "static",
            ]
        )

    # get_final_states is utility function that returns final state of transition table.
    def get_final_states(self, name_of_rule):
        return self.table[name_of_rule]["final"]


if __name__ == "__main__":
    table = TransitionTable()
    print("======================================================")
    print(table.table)
    print("======================================================")
    print(table.get_final_states("KEYWORD"))
    print("======================================================")
