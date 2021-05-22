# -*- coding: utf-8 -*-


from transtable import TransitionTable

# DFA class implements the action of DFA.
class DFA:
    # DFA is initialized with following variables.
    # - name : DFA's name
    # - alphabet : Whole set of alphabet that this dfa can handle.
    # - transition_table : Transition table is python dictionary
    #                      which is reduced by this DFA. DFA references transition table.
    # - initial_state : Literally, this is initial state of DFA.
    # - final_state : List of final state.
    def __init__(self, name, alphabet, transition_table, initial_state, final_state):
        self.name = name
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.state = initial_state
        self.initial_state = initial_state
        self.final_state = final_state
        # We defined running state of DFA for check if DFA is running.
        # This is used when accept token.
        self.running = True

    # run function gets input string and perform transition.
    # This function returns the running state of DFA which can help lexical analyzer
    # configure this DFA is running or not.
    def run(self, inputValue):
        # If DFA is not running, we don't need to process input value.
        if not self.running:
            # print(f"{self.name} is not running")
            return False

        # If inputValue is not defined in alphabet, we don't need to process input value.
        if inputValue not in self.alphabet:
            # print(f"{self.name} dfa have error | {inputValue}: undefined alphabet")
            self.running = False
            return False

        # If there's no condition that stops DFA, proceed.
        # From transition table, get state and transition key as key-value.
        for old_state, transitions in self.transition_table.items():
            # print(f"{old_state} : {transitions}")
            # If current state is same as the state that is taken from transition table,
            # we need to check if DFA is transitable.
            if old_state == self.state:
                # Get transition key and new state from transition table.
                for key, new_state in transitions.items():
                    # If input value is transition key,
                    if inputValue in key:
                        # Change the state of this DFA.
                        self.state = new_state
                        # print(f"Transition Success! from {old_state} to {self.state}")
                        # And return true to notify this DFA is alive.
                        return True

        # If we couldn't process anything at for loop. this means somthing went wrong.
        # So set the running state of DFA as False and return False.
        else:
            self.running = False
            return False

    # Allow to reset DFA with this reset function so that
    # change DFA's running state to True again after
    # get one Token.
    def reset(self):
        self.state = self.initial_state
        self.running = True

    # Return if DFA processing is done by checking the state is final state at that time.
    def isDone(self):
        return self.running and self.state in self.final_state


class SlrDFA:
    def __init__(self, name, alphabet, transition_table, initial_state, final_state):
        self.name = name
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.state = initial_state
        self.initial_state = initial_state
        self.final_state = final_state
        self.running = True

    def run(self, inputValue):
        if not self.running:
            print("Not running")
            return False, None

        if inputValue not in self.alphabet:
            print("Not alphabet")
            self.running = False
            return False, None

        for old_state, transitions in self.transition_table.items():
            if old_state == self.state:
                for key, valueTuple in transitions.items():
                    if inputValue == key:
                        return True, valueTuple

        else:
            self.running = False
            return False, None

    def setState(self, newState):
        self.state = newState

    def reset(self):
        self.state = self.initial_state
        self.running = True, None

    def isDone(self):
        return self.running and self.state == self.final_state
