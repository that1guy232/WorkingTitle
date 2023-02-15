import pygame

from Trengine.GameRenderer.Renderable import Renderable


class Renderer:
 
    def __init__(self, display, camera):
     
        self.display = display
       
        self.camera = camera
     
        self.renderables = []

    def draw(self):
        # update the camera 
        self.camera.update()
        # draw the renderables
        for renderable in self.renderables:
            offset = renderable.posistion - self.camera.posistion
            # apply the zoom
            renderable.draw(self.display, offset, self.camera.zoom)
            #renderable.render(self.display, self.camera.posistion)

    def add(self, renderable):
        # make sure it's a renderable
        if isinstance(renderable, Renderable):
            self.renderables.append(renderable)
        else:
            raise TypeError("Renderable must be a Renderable object")

    def remove(self, renderable):
        if renderable in self.renderables:
            self.renderables.remove(renderable)
        #self.renderables.remove(renderable)