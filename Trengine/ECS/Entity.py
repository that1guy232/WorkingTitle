from Trengine.ECS.Component import Component

# define the entities


class Entity:
    def __init__(self):
        self.components = []

    def add_component(self, component: Component):
        self.components.append(component)

    def has_components(self, components):
        for component in components:
            if not self.has_component(component):
                return False
        return True

    def has_component(self, component):
        for c in self.components:
            if c.name == component:
                return True
        return False

    def get_component(self, component):
        for c in self.components:
            if c.name == component:
                return c
        return None
