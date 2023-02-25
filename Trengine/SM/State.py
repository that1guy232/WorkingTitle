class State:

    def __init__(self, name, on_enter=None, on_exit=None):
        self.name = name
        if on_enter is not None:
            self.on_enter = on_enter

        if on_exit is not None:
            self.on_exit = on_exit

    def set_on_enter(self, on_enter):
        self.on_enter = on_enter

    def set_on_exit(self, on_exit):
        self.on_exit = on_exit

    def on_enter(self):
        print(f"Entering state {self.name}")

    def on_exit(self):
        print(f"Exiting state {self.name}")
