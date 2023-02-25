import pygame

class SpriteSheet:
    def __init__(self, filename, tile_size, tile_padding):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.tile_size = tile_size
        self.tile_padding = tile_padding

    def get_tile(self, x, y):
        return self.sheet.subsurface((x * self.tile_size + x * self.tile_padding, y * self.tile_size + y * self.tile_padding, self.tile_size, self.tile_size))
