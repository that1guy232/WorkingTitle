class GameScene():
    def __init__(self, game,name) -> None:
        self.game = game
        self.name = name
        self.clear_color = (0, 0, 0)
        self.UIWidgets = []

        pass

    def update(self):
        pass

    def draw(self):
        # clear the screen
        self.game.screen.fill(self.clear_color)

        for widget in self.UIWidgets:
            widget.draw(self.game.screen)
        pass

    def handle_event(self, event):

        for widget in self.UIWidgets:
            widget.handle_event(event)
            pass
        
        pass

    pass