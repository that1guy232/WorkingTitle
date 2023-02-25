from Trengine.ECS.System import System

from Trengine.ECS.common.components.SpriteComponent import SpriteComponent
from Trengine.ECS.common.components.PositionComponent import PositionComponent

from Trengine.ECS.Entity import Entity

from Trengine.Game.GameScene import GameScene

from Trengine.GameRenderer.Renderable import Texture

import pygame


class SpriteRenderSystem(System):
    def __init__(self, game_scene: GameScene) -> None:
        super().__init__()

        self.game_scene = game_scene

        self.required_components = [
            "SpriteComponent",
            "PositionComponent"
        ]

        self.renderable_entities = []

        # get the renderable entities
        entity: Entity
        for entity in self.game_scene.ECSWorld.entities:
            if entity.has_components(self.required_components):
                self.renderable_entities.append(entity)
                pass
            pass

        pass

    def add_entity(self, entity: Entity):
        if entity.has_components(self.required_components):
            self.renderable_entities.append(entity)
            self.on_entity_added(entity)
            return True
        else:
            return False

    def on_entity_added(self, entity: Entity):

        ent_sprite = entity.get_component("SpriteComponent").sprite
        ent_pos = entity.get_component("PositionComponent")
        # create a renderable for the sprite
        # x,y of the enty, width & height of the sprite and the sprite itself

        renderable = Texture(ent_pos.x, ent_pos.y, ent_sprite.get_width(), ent_sprite.get_height(), ent_sprite)
        self.game_scene.renderables.append(renderable)


        # self.game_scene.renderables.append(entity.get_component("SpriteComponent").sprite)
        pass

    def update(self, dt):
        entity: Entity
      
        for entity in self.renderable_entities:
          
            sprite_component = entity.get_component("SpriteComponent")
            position_component = entity.get_component("PositionComponent")
            
            # self.game_scene.game.screen.blit(
            #     sprite_component.sprite, (position_component.x, position_component.y))
        pass
    pass
