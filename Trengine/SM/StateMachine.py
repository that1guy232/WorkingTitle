class StateMachine:
    def __init__(self) -> None:
        self.states = {}
        self.state_stack = []
        pass

    def push_state(self, state):
        self.state_stack.append(state)
        state.on_enter()
        pass

    def pop_state(self, state=None):
        if state == None:
            self.state_stack[-1].on_exit()
            self.state_stack.pop()

        else:
            # find the state in the stack
            for i in range(len(self.state_stack)):
                if self.state_stack[i] == state:
                    self.state_stack[i].on_exit()
                    self.state_stack.pop(i)
                    break
                pass
        pass

    # a function to determine if a state is on the stack

    def is_state_on_stack(self, state):
        return state in self.state_stack
        pass

    pass
