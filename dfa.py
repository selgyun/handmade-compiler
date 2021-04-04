# -*- coding: utf-8 -*-


from transtable import TransitionTable


class DFA:
    def __init__(self, name, alphabet, transition_table, initial_state, final_state):
        self.name = name
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.state = initial_state
        self.final_state = final_state
        self.running = True

    # get input string and perform transition
    def run(self, input):
        for c in input:
            if not self.running:
                print(f"{self.name} is not running")
                self.running = False
                return False

            # c is not defined in alphabet
            if c not in self.alphabet:
                print(f"{self.name}|{c}: undefined alphabet")
                self.running = False
                return False

            for old_state, transitions in self.transition_table.items():
                print(f"{old_state} : {transitions}")
                if old_state == self.state:
                    for key, new_state in transitions.items():
                        if c in key:
                            self.state = new_state
                            print(
                                f"Transition Success! from {old_state} to {self.state}"
                            )
                            return True

            else:
                self.running = False
                return False

    def isDone(self):
        return self.running and self.state == self.final_state
