from Trengine.Game.GameScene import GameScene

# ECS imports
from Trengine.ECS.World import World as ECSWorld

# Components
from Trengine.ECS.common.components.PositionComponent import PositionComponent
from Trengine.ECS.common.components.VelocityComponent import VelocityComponent
from Trengine.ECS.common.components.SpriteComponent import SpriteComponent

# Systems
from Trengine.ECS.common.systems.SpriteRenderSystem import SpriteRenderSystem



#SM imports
from Trengine.SM.StateMachine import StateMachine
from Trengine.SM.State import State

import pygame


class PlayScene(GameScene):
    def __init__(self, game, name) -> None:
        super().__init__(game, name)



        self.colors = {
            "sky_blue": (135, 206, 235)
        }

        self.clear_color = self.colors["sky_blue"]

        self.ECSWorld = ECSWorld()

        ent1 = self.ECSWorld.create_entity()
        ent1.add_component(PositionComponent(0, 0))
        ent1.add_component(VelocityComponent(0, 0))
        plrspr = pygame.image.load("game/assets/player.png")
        ent1.add_component(SpriteComponent(plrspr))

        self.ECSWorld.add_system(SpriteRenderSystem())
        
        
        self.game_states = [
            State("playing"),
            State("paused")
        ]

        self.state_machine = StateMachine()

        self.state_machine.push_state(self.game_states[0])

        # add all the states to the state machine
        for state in self.game_states:
            self.state_machine.add_state(state.name, state)
            pass

        

        pass

    def update(self, dt):
        # print the state stack names
        # if there is no paused state, then the game is playing
        paused = False
        for state in self.state_machine.state_stack:
            if state.name == "paused":
                paused = True
                pass
            pass

        if not paused:
            self.ECSWorld.update(dt)
            pass

    def draw(self):
        super().draw()
        pass

    def handle_event(self, event):
        super().handle_event(event)
        # if the escape key is pressed, push the paused state onto the stack
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # push or pop the paused state
                if self.state_machine.state_stack[-1].name == "paused":
                    self.state_machine.pop_state()
                    pass
                else:
                    self.state_machine.push_state(self.game_states[1])
                    pass
            pass
    pass