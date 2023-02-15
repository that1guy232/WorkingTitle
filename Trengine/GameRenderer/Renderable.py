from matplotlib import widgets
import pygame
# ineratable class


class Renderable:
    def __init__(self, x, y, width, height):
        self.posistion = pygame.Vector2(x, y)
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, display, offset):
        pass


class Box(Renderable):
    def __init__(self, x, y, width, height, color = (255, 255, 255), line_width = 0):
        super().__init__(x, y, width, height)
        self.width = width
        self.height = height
        self.color = color
        self.line_width = line_width

    def draw(self, display, offset, zoom):
        # mulitply are x and y by the zoom
        x = self.posistion.x * zoom
        y = self.posistion.y * zoom
        # apply the offset
        x += offset.x
        y += offset.y

        # draw the box
        pygame.draw.rect(display, self.color, (x, y, self.width * zoom, self.height * zoom), self.line_width)
        

class Circle(Renderable):
    def __init__(self, x, y, radius, color = (255, 255, 255), line_width = 0):
        super().__init__(x, y, radius, radius)
        self.radius = radius
        self.color = color
        self.line_width = line_width

    def draw(self, display, offset, zoom):
        # mulitply are x and y by the zoom
        x = self.posistion.x * zoom
        y = self.posistion.y * zoom
        # apply the offset
        x += offset.x
        y += offset.y

        # draw the circle
        pygame.draw.circle(display, self.color, (x, y), self.radius * zoom, self.line_width)

class Polygon(Renderable):
    def __init__(self, x, y, points):
        super().__init__(x, y, 0, 0)
        self.points = points

    def draw(self, display, offset, zoom):
        # mulitply are x and y by the zoom
        x = self.posistion.x * zoom
        y = self.posistion.y * zoom
        # apply the offset
        x += offset.x
        y += offset.y

        # draw the polygon outline
        pygame.draw.polygon(display, (255, 255, 255), [
                            (x + point.x * zoom, y + point.y * zoom) for point in self.points], 1)

class Texture(Box):
    def __init__(self, x, y, width, height, texture):
        super().__init__(x, y, width, height)
        self.texture = texture
        self.last_zoom = 0
    def draw(self, display, offset, zoom):
        # mulitply are x and y by the zoom
        x = self.posistion.x * zoom
        y = self.posistion.y * zoom
        # apply the offset
        x += offset.x
        y += offset.y


        #self.texture = pygame.transform.scale(self.texture, (self.width * zoom, self.height * zoom))
        # pygame.transform.scale is a bit slow, so we only want to call it when we need to, so we check if the zoom has changed
        if self.last_zoom != zoom:
            self.texture = pygame.transform.scale(self.texture, (self.width * zoom, self.height * zoom))
            self.last_zoom = zoom
            

        self.last_zoom = zoom

        display.blit(self.texture, (x, y), (0, 0, self.width * zoom, self.height * zoom))