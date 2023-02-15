from Trengine.ECS.Component import Component

class SpriteComponent(Component):
    def __init__(self, sprite) -> None:
        self.sprite = sprite
        pass