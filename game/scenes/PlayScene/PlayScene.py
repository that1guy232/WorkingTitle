from Treengine.Game.GameScene import GameScene

"""
Metroidvania is a sub-genre of action-adventure games and/or platformers focused on guided non-linearity and utility-gated exploration and progression. 
"""

from Treengine.UI.Button import Button

# ECS imports
from Treengine.ECS.World import World as ECSWorld

# Components
# common
from Treengine.ECS.common.components.PositionComponent import PositionComponent
from Treengine.ECS.common.components.VelocityComponent import VelocityComponent
from Treengine.ECS.common.components.SpriteComponent import SpriteComponent

# game specific
from game.ECS.components.PlayerComponent import PlayerComponent

# Systems
# common
from Treengine.ECS.common.systems.SpriteRenderSystem import SpriteRenderSystem

# game specific
from game.ECS.systems.PlayerInputSystem import PlayerInputSystem


# SM imports
from Treengine.SM.StateMachine import StateMachine
from Treengine.SM.State import State

from Treengine.Game.Tiles import TileDict
from Treengine.Game.Spritesheet import SpriteSheet

# to load the player sprite
import pygame


class PlayScene(GameScene):
    def __init__(self, game, name) -> None:
        super().__init__(game, name)

        self.colors = {
            "sky_blue": (135, 206, 235),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            # dark gray for the landscape
            "dark_gray": (50, 50, 50),
            # debug magenta
            "debug": (255, 0, 255),
        }

        self.clear_color = self.colors["dark_gray"]

        self.ECSWorld = ECSWorld()

        self.entities = []

        self.dt = 0

        self.paused = False

        self.sprite_sheet = SpriteSheet("game/assets/colored-transparent.png", 16, 1)

        self.tile_dict = TileDict("game/assets/tiles.txt")

        # self.map = TileMap("game/assets/map.txt")

        # create a renderable for the first tile in the tile dict
        test_tile = self.tile_dict.tiles[0].surface

        # print the flags of the first tile
        print("Flags: ", self.tile_dict.tiles[0].flags)

        player_ent = self.ECSWorld.create_entity()
        player_ent.add_component(PositionComponent(100, 100))
        plr_spr = self.sprite_sheet.get_tile(25, 0)
        player_ent.add_component(SpriteComponent(test_tile))
        print(plr_spr)
        player_ent.add_component(PlayerComponent())

        self.sprite_render_system = SpriteRenderSystem(self)
        self.sprite_render_system.add_entity(player_ent)

        self.ECSWorld.add_system(self.sprite_render_system)
        self.ECSWorld.add_system(PlayerInputSystem(self.game))

        self.game_states = {"playing": State("playing"), "paused": State("paused")}

        self.state_machine = StateMachine()

        # exit game button callback

        def exit_game():
            self.game.transition_to_scene("main_scene")
            pass

        self.paused_buttons = [
            # exit game button
            Button(350, 250, 100, 50, (255, 0, 0), "Exit", exit_game)
        ]

        # add the paused buttons to the UI
        for button in self.paused_buttons:
            self.UIWidgets.append(button)
            button.hidden = True

        pass

    def on_enter(self):
        self.game.camera.zoom = 2
        self.state_machine.push_state(self.game_states["playing"])

        # super().on_enter()

    def update(self, dt):
        self.dt = dt
        # if there is no paused state, then the game is playing
        for state in self.state_machine.state_stack:
            if state.name == "paused":
                self.paused = True
                # set the paused buttons to visible
                for button in self.paused_buttons:
                    button.hidden = False
                    pass
                pass
            else:
                self.paused = False
                # set the paused buttons to hidden
                for button in self.paused_buttons:
                    button.hidden = True
                    pass
                pass
            pass

        if not self.paused:
            # black list sprites from being updated than update everything else
            self.ECSWorld.update(
                self.dt, list_components=["SpriteComponent"], whitelist_flag=False
            )

    def draw(self):
        # draw the first tile in the tile dictionary

        # draw a tile at the mouse position
        mouse_pos = pygame.mouse.get_pos()

        super().draw()

        self.ECSWorld.update(
            self.dt, list_components=["SpriteComponent"], whitelist_flag=True
        )

        pass

    def handle_event(self, event):
        super().handle_event(event)
        # if the escape key is pressed, push the paused state onto the stack
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # push or pop the paused state
                if self.state_machine.is_state_on_stack(self.game_states["paused"]):
                    self.state_machine.pop_state(state=self.game_states["paused"])
                    pass
                else:
                    self.state_machine.push_state(self.game_states["paused"])

                pass
            pass

    pass
