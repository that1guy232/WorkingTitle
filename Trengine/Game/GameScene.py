import pygame


class GameScene():
    def __init__(self, game, name) -> None:
        self.game = game
        self.name = name
        self.clear_color = (0, 0, 0)
        self.UIWidgets = []

        self.renderables = []

        pass

    def on_enter(self):
        # reset the camera
        self.game.camera.posistion = pygame.Vector2(0, 0)
        self.game.camera.zoom = 1

        pass

    def on_exit(self):
        pass

    def update(self):
        pass

    def draw(self):
        # clear the screen
        self.game.screen.fill(self.clear_color)

        # draw all the renderables
        for renderable in self.renderables:

            renderable.draw(self.game.screen,
                            self.game.camera.posistion, self.game.camera.zoom)
            pass

        # draw all the UI widgets
        for widget in self.UIWidgets:
            widget.draw(self.game.screen)
        pass

    def handle_event(self, event):

        for widget in self.UIWidgets:
            widget.handle_event(event)
            pass

        pass

    pass
