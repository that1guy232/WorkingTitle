class StateMachine:
    def __init__(self) -> None:
        self.states = {}
        self.state_stack = []
        pass

    def add_state(self, name, state):
        self.states[name] = state
        pass
    
    def push_state(self, state):
        self.state_stack.append(state)
        state.on_enter()
        pass

    def pop_state(self):
        self.state_stack[-1].on_exit()
        self.state_stack.pop()

        pass

    pass

