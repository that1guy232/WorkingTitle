from Treengine.GameRenderer.Renderable import Texture
from Treengine.GameRenderer.Renderable import Box

from Treengine.Game.SceneState import SceneState


class TileCreateState(SceneState):
    def __init__(self, editor_scene) -> None:
        super().__init__("tile_create", editor_scene)
        self.editor_scene = editor_scene

        spritesheet_surface = editor_scene.sprite_sheet.sheet
        spritesheet_width = spritesheet_surface.get_width()
        spritesheet_height = spritesheet_surface.get_height()

        self.SpriteSheet_texture = Texture(
            0, 0, spritesheet_width, spritesheet_height, spritesheet_surface
        )

        self.hightlighted_tile = Box(
            0,
            0,
            editor_scene.sprite_sheet.tile_size,
            editor_scene.sprite_sheet.tile_size,
            visible=False,
        )

    def on_enter(self):
        # add the sprite sheet texture to the renderables
        self.editor_scene.renderables.append(self.SpriteSheet_texture)
        pass

    def on_exit(self):
        # remove the sprite sheet texture from the renderables
        self.editor_scene.renderables.remove(self.SpriteSheet_texture)

        pass

    def update(self, dt):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        pass

    pass
