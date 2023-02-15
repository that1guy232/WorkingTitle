from Trengine.Game.GameScene import GameScene

from Trengine.UI.Button import Button


class MainMenu(GameScene):
    def __init__(self, game,name) -> None:   
        super().__init__(game, name)

        # Play button

        def start_button_callback():
            game.transition_to_scene("game_scene")
            pass

        self.UIWidgets.append(
            Button(100, 100, 100, 50, (255, 0, 0), "Start", start_button_callback))

        # Settings button

        def settings_button_callback():
            pass

        self.UIWidgets.append(
            Button(100, 200, 100, 50, (255, 0, 0), "Settings", settings_button_callback))

        # Exit button

        def exit_button_callback():
            self.game.running = False
            pass

        self.UIWidgets.append(
            Button(100, 300, 100, 50, (255, 0, 0), "Exit", exit_button_callback))

        pass

    def update(self,dt):
        #super().update(dt)
        pass

    def draw(self):
        super().draw()
        pass

    def handle_event(self, event):
        super().handle_event(event)
        pass
    pass
