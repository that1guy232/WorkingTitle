from Trengine.ECS.Component import Component

# define the entities
class Entity:
    def __init__(self):
        self.components = []

    def add_component(self, component: Component):
        self.components.append(component)