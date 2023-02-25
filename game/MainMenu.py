from Trengine.Game.GameScene import GameScene

from Trengine.UI.Button import Button

from Trengine.GameRenderer.Renderable import Texture

import pygame


class MainMenu(GameScene):
    def __init__(self, game, name) -> None:
        super().__init__(game, name)
        self.test = True

        #self.title_image = pygame.image.load("game/assets/title.png")

        #self.renderables.append(Texture(0, 0, 800, 600, self.title_image))
        # Play button

        def start_button_callback():
            game.transition_to_scene("game_scene")
            pass

        self.UIWidgets.append(
            Button(100, 300, 100, 50, (255, 0, 0), "Start", start_button_callback))

        # Settings button

        def settings_button_callback():
            pass

        self.UIWidgets.append(
            Button(350, 300, 100, 50, (255, 0, 0), "Settings", settings_button_callback))

        # Exit button

        def exit_button_callback():
            self.game.running = False
            pass

        self.UIWidgets.append(
            Button(600, 300, 100, 50, (255, 0, 0), "Exit", exit_button_callback))

        # a button for a level editor

        def level_editor_button_callback():
            game.transition_to_scene("level_editor")
            pass

        self.UIWidgets.append(
            Button(100, 400, 100, 50, (255, 0, 0), "Editor", level_editor_button_callback))

        pass

    def update(self, dt):
        # super().update(dt)
        pass

    def draw(self):
        super().draw()
        #self.game.screen.blit(self.title_image, (0, 0))
        pass

    def handle_event(self, event):
        super().handle_event(event)
        pass
    pass
