from Treengine.ECS.System import System


class PlayerInputSystem(System):
    def __init__(self, game) -> None:
        super().__init__()

        self.game = game

        self.required_components = ["PlayerComponent"]
        pass

    def update(self, dt):
        # print(self.game.events)
        pass

    pass
