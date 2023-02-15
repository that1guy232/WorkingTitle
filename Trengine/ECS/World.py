from Trengine.ECS.Component import Component
from Trengine.ECS.System import System
from Trengine.ECS.Entity import Entity

# define the world
class World:
    def __init__(self):
        self.entities = []
        self.systems = []

    def create_entity(self) -> Entity:
        entity = Entity()
        self.entities.append(entity)
        return entity

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def add_system(self, system: System):
        self.systems.append(system)

    def update(self,dt):
        for system in self.systems:
            system.update(dt)