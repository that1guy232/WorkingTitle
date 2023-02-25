from Trengine.ECS.Component import Component


class VelocityComponent(Component):
    def __init__(self, x, y) -> None:
        super().__init__("VelocityComponent")
        self.x = x
        self.y = y
        pass
