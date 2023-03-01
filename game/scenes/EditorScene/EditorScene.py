from Treengine.Game.GameScene import GameScene


from Treengine.Game.Spritesheet import SpriteSheet

from game.scenes.EditorScene.States.TileCreateState import TileCreateState


class EditorScene(GameScene):
    def __init__(self, game, name) -> None:
        super().__init__(game, name)

        sprite_sheet_padding = 1
        sprite_sheet_tile_size = 16

        self.sprite_sheet = SpriteSheet(
            "game/assets/colored-transparent.png",
            sprite_sheet_tile_size,
            sprite_sheet_padding,
        )

        pass

    def on_enter(self):
        super().on_enter()

    def on_exit(self):
        super().on_exit()

    def update(self, dt):
        super().update(dt)
        pass

    def draw(self):
        super().draw()

        pass

    def handle_event(self, event):
        super().handle_event(event)

        pass
