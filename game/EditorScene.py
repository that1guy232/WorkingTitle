from Trengine.Game.GameScene import GameScene

from Trengine.GameRenderer.Renderable import Texture
from Trengine.GameRenderer.Renderable import Text
from Trengine.GameRenderer.Renderable import Box

from Trengine.SM.StateMachine import StateMachine
from Trengine.SM.State import State

from Trengine.Game.Spritesheet import SpriteSheet

import pygame


class EditorScene(GameScene):
    def __init__(self, game, name) -> None:

        super().__init__(game, name)

        self.setup_states()
        # a function that we will use to set up are sta
        # tile Creator stuff

        sprite_sheet_padding = 1
        sprite_sheet_tile_size = 16
        self.sprite_sheet = SpriteSheet(
            "game/assets/colored-transparent.png", sprite_sheet_tile_size, sprite_sheet_padding)
        spritesheet_surface = self.sprite_sheet.sheet
        spritesheet_width = spritesheet_surface.get_width()
        spritesheet_height = spritesheet_surface.get_height()
        SpriteSheet_texture = Texture(
            0, 0, spritesheet_width, spritesheet_height, spritesheet_surface)

        self.renderables.append(SpriteSheet_texture)

        self.tile_outlines = []

        # # create a bunch oof base outlines to cover the sprite sheet taking into account the tile spacing
        for x in range(0, spritesheet_width, sprite_sheet_tile_size + sprite_sheet_padding):
            for y in range(0, spritesheet_height, sprite_sheet_tile_size + sprite_sheet_padding):
                self.tile_outlines.append(
                    Box(x, y, sprite_sheet_tile_size, sprite_sheet_tile_size, (255, 255, 255), 1))

        for outline in self.tile_outlines:
            outline.is_visible = False
            self.renderables.append(outline)

        # text

        self.controll_string = ""

        self.text = Text(0, 0, self.controll_string, pygame.font.Font(
            pygame.font.get_default_font(), 25))
        self.text.ignore_camera = True

        self.renderables.append(self.text)

        pass

    # a function that we will use to set up are states
    def setup_states(self):
        self.state_machine = StateMachine()

        self.valid_states = {
            "main": State("main"),
            "make_tile": State("make_tile"),
        }

        # set set the on enter and on exit functions for the states

        def on_mainstate_enter():
            print("entering main state")

        self.valid_states["main"].set_on_enter(on_mainstate_enter)

        pass

    def on_enter(self):
        super().on_enter()
        # Push the main state
        self.state_machine.push_state(self.valid_states["main"])

    def update(self, dt):
        # update depending on the current state
        # we should alway's have the main state unless we are are going to a new scene
        # so if it is on the stack then we are in the main state
        if self.state_machine.is_state_on_stack(self.valid_states["main"]):

            pass
        else:
            # switch to the title screen
            self.game.transition_to_scene("main_scene")
            pass

        pass

    def draw(self):
        super().draw()

        pass

    def handle_event(self, event):
        super().handle_event(event)
        # if the mouse wheel is scrolled zoom in or out
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.game.camera.zoom += 0.1
            elif event.button == 5:
                self.game.camera.zoom -= 0.1

        # if esc key is pressed pop states
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.state_machine.pop_state()

            # wasd to move the camera
            if event.key == pygame.K_s:
                self.game.camera.move((0, -16))
            if event.key == pygame.K_w:
                self.game.camera.move((0, 16))
            if event.key == pygame.K_d:
                self.game.camera.move((-16, 0))
            if event.key == pygame.K_a:
                self.game.camera.move((16, 0))

        # if the mouse is moved
        if event.type == pygame.MOUSEMOTION:
            # is the mouse over one of the tile outlines
            for outline in self.tile_outlines:
                mouse_pos = pygame.mouse.get_pos()
                world_mouse_pos = self.game.camera.screen_to_world(mouse_pos)
                outline_rec = pygame.Rect(
                    outline.posistion.x, outline.posistion.y, outline.width, outline.height)
                if not outline_rec.collidepoint(world_mouse_pos):
                    outline.color = (255, 255, 255)
                    outline.line_width = 1
                    outline.is_visible = False

                else:
                    outline.color = (255, 0, 0)
                    outline.line_width = 2
                    outline.is_visible = True
                    print(outline.posistion // 16)
