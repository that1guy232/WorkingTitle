
# x, y, width, height, color, text, callback
import pygame


class Button:
    
    '''
    x (int): The x-coordinate of the top-left corner of the button.
    y (int): The y-coordinate of the top-left corner of the button.
    width (int): The width of the button in pixels.
    height (int): The height of the button in pixels.
    color (tuple): The color of the button in RGB format.
    text (str): The text that will be displayed on the button.
    callback (function): The function that will be called when the button is clicked.
    '''

    def __init__(self, x, y, width, height, color, text, callback):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.callback = callback
        self.font = pygame.font.SysFont("comicsans", 20)

    def draw(self, surface):
        # draw the text
        text = self.font.render(self.text, 1, (0, 0, 0))
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height))
        surface.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                     self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.is_over(event.pos):
                    self.callback()
