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
