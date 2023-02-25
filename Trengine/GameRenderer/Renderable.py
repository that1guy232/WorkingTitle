from matplotlib import widgets
import pygame
# ineratable class


class Renderable:
    def __init__(self, x, y, width, height):
        self.posistion = pygame.Vector2(x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.ignore_camera = False
        self.is_visible = True

    def draw(self):
        pass

    def copy(self, x, y):
        return self.__class__(x, y, self.width, self.height, self.color, self.line_width)


class Box(Renderable):
    '''
    Parameters

    x (int): The x-coordinate of the top-left corner of the box.
    y (int): The y-coordinate of the top-left corner of the box.
    width (int): The width of the box in pixels.
    height (int): The height of the box in pixels.
    color (tuple): The color of the box in RGB format.
    line_width (int): The width of the box's outline in pixels.
    '''

    def __init__(self, x, y, width, height, color=(255, 255, 255), line_width=0):
        super().__init__(x, y, width, height)
        self.width = width
        self.height = height
        self.color = color
        self.line_width = line_width

    def draw(self, display, offset, zoom):
            
        if not self.is_visible:
            return

        # mulitply are x and y by the zoom
        x = self.posistion.x * zoom
        y = self.posistion.y * zoom
        # apply the offset
        x += offset.x
        y += offset.y

        # draw the box
        pygame.draw.rect(display, self.color, (x, y, self.width *
                         zoom, self.height * zoom), self.line_width)


class Circle(Renderable):
    def __init__(self, x, y, radius, color=(255, 255, 255), line_width=0):
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
        pygame.draw.circle(display, self.color, (x, y),
                           self.radius * zoom, self.line_width)


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
        self.scaled_texture = texture
        self.last_zoom = 0

    def draw(self, display, offset, zoom):
        # mulitply are x and y by the zoom
        x = self.posistion.x * zoom
        y = self.posistion.y * zoom
        # apply the offset
        x += offset.x
        y += offset.y

        # self.texture = pygame.transform.scale(self.texture, (self.width * zoom, self.height * zoom))
        # pygame.transform.scale is a bit slow, so we only want to call it when we need to, so we check if the zoom has changed

        # if the zoom is going to be less than 0, keep it at the last zoom
        if zoom < 0:
            zoom = self.last_zoom

        if self.last_zoom != zoom:
            self.scaled_texture = pygame.transform.scale(
                self.texture, (self.width * zoom, self.height * zoom))
            self.last_zoom = zoom

        self.last_zoom = zoom

        display.blit(self.scaled_texture, (x, y),
                     (0, 0, self.width * zoom, self.height * zoom))


class Text(Renderable):
    '''

    '''

    def __init__(self, x, y, text, font, color=(255, 255, 255)):
        super().__init__(x, y, 0, 0)
        self.text = text
        self.font = font
        self.color = color
        self.last_zoom = 0

    def draw(self, display, offset, zoom):
        if not self.is_visible:
            return

        if self.ignore_camera:
            offset = pygame.Vector2(0, 0)
            zoom = 1
        pass

        # mulitply are x and y by the zoom
        x = self.posistion.x * zoom
        y = self.posistion.y * zoom
        # apply the offset
        x += offset.x
        y += offset.y

        # we need to manually split the text into lines new lines, font.render doesn't do this for us :(
        lines = self.text.split("\n")
        # print the lines
        for line in lines:
            # blit the line one below the other
            display.blit(self.font.render(line, True, self.color), (x, y))
            # add the height of the line to the y posistion
            y += self.font.get_height()
