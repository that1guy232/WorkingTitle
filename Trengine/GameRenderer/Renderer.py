import pygame
from Trengine.GameRenderer.Renderable import Renderable


class Renderer:
    """
    A class that manages a list of Renderable objects and renders them to a display using a Camera object.

    Attributes:
        display (pygame.Surface): The display to which the Renderer object will render.
        camera (Camera): The Camera object to use for rendering.
        renderables (list): A list of Renderable objects that the Renderer will render.

    Methods:
        draw(): Renders all the Renderable objects in the renderables list to the display.
        add(renderable): Adds a Renderable object to the renderables list.
        remove(renderable): Removes a Renderable object from the renderables list.

    """

    def __init__(self, display, camera):
        """
        Initializes the Renderer object with the given display and Camera object.

        Args:
            display (pygame.Surface): The display to which the Renderer object will render.
            camera (Camera): The Camera object to use for rendering.
        """
        self.display = display
        self.camera = camera
        self.renderables = []

    def draw(self):
        """
        Renders all the Renderable objects in the renderables list to the display.
        """
        # Update the camera
        self.camera.update()

        # Draw the renderables
        for renderable in self.renderables:
            # Calculate the offset between the renderable object's position and the camera's position
            offset = renderable.posistion - self.camera.posistion

            # Apply the zoom to the renderable object's position
            renderable.draw(self.display, offset, self.camera.zoom)

    def add(self, renderable):
        """
        Adds a Renderable object to the renderables list.

        Args:
            renderable (Renderable): The Renderable object to add to the renderables list.

        Raises:
            TypeError: If the given object is not a Renderable object.
        """
        # Make sure the given object is a Renderable object
        if isinstance(renderable, Renderable):
            self.renderables.append(renderable)
        else:
            raise TypeError("Renderable must be a Renderable object")

    def remove(self, renderable):
        """
        Removes a Renderable object from the renderables list.

        Args:
            renderable (Renderable): The Renderable object to remove from the renderables list.
        """
        if renderable in self.renderables:
            self.renderables.remove(renderable)
