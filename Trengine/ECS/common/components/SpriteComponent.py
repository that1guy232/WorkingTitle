from Trengine.ECS.Component import Component


class SpriteComponent(Component):
    def __init__(self, sprite) -> None:
        super().__init__("SpriteComponent")
        self.sprite = sprite
        pass
    pass