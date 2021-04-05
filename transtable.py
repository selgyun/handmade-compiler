# -*- coding: utf-8 -*-
import string


# build_transition_table_with_lexemes build transition table
# very easily from lexemes.
# You can pass lexemes of the rule.
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
        self.table = {
            "SINGLE_CHARACTER": {
                0: {"'": 1},
                1: {string.ascii_letters: 3, string.digits: 2, " ": 4},
                2: {"'": 5},
                3: {"'": 5},
                4: {"'": 5},
                5: {},
                "final": [5],
            }
        }

        self.table["KEYWORD"] = build_transition_table_with_lexemes(
            ["if", "else", "while"]
        )

    def get_final_states(self, name_of_rule):
        return self.table[name_of_rule]["final"]


if __name__ == "__main__":
    table = TransitionTable()
    print("======================================================")
    print(table.table)
    print("======================================================")
    print(table.get_final_states("KEYWORD"))
    print("======================================================")
    
