class State:
    def __init__(self, name):
        self.name = name

    def on_enter(self):
        print(f"Entering state {self.name}")

    def on_exit(self):
        print(f"Exiting state {self.name}")