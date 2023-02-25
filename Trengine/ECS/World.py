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

    def update(self, dt, list_components=None, whitelist_flag=False):

        for system in self.systems:
            # if the system requires components
            if len(system.required_components) > 0:
                if not whitelist_flag:
                    # we are a blacklist
                    # if the system does not require any of the components in the list, we update it
                    if not any(c in list_components for c in system.required_components):
                        system.update(dt)
                    pass

                else:
                    # we are a whitelist
                    # if the system requires any of the components in the list, we update it
                    if any(c in list_components for c in system.required_components):
                        system.update(dt)
                    pass
