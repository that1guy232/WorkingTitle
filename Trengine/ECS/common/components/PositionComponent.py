from Trengine.ECS.Component import Component


class PositionComponent(Component):
    def __init__(self, x, y) -> None:
        super().__init__("PositionComponent")
        self.x = x
        self.y = y
        pass
