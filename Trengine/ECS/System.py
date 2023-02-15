from Trengine.ECS.Entity import Entity

# define the base system
class System:
    def __init__(self):
        self.entities = []
        # define the required components for this system, these will be checked when adding an entity to the system
        self.required_components = []


    def add_required_component(self, component):
        self.required_components.append(component)

    def add_entity(self, entity: Entity):
        # check if the entity has all the required components
        for component in self.required_components:
            if not entity.has_component(component):
                return False
            else:
                self.entities.append(entity)
                return True
            
    def update(self, dt):
        pass
