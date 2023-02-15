from pyautogui import PRIMARY
import pygame


class Camera:
    def __init__(self, width, height, camera_min_x, camera_min_y, camera_max_x=10000000, camera_max_y=10000000):
        self.width = width
        self.height = height
        self.posistion = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.zoom = 1
        self.rect = pygame.Rect(
            self.posistion.x, self.posistion.y, width, height)
        self.camera_min_y = camera_min_y
        self.camera_max_y = camera_max_y
        self.camera_min_x = camera_min_x
        self.camera_max_x = camera_max_x
        self.camera_rotation = 0

    def update(self):

        # dont go below 0.1 zoom
        if self.zoom < 0.5:
            self.zoom = 0.5
        self.old_posistion = self.posistion

    # a function to move the camera by a delta vector

    def move(self, delta):
        self.posistion += delta

    def screen_to_world(self, pos):
        pos = pygame.Vector2(pos)
        pos.x = (pos.x - self.posistion.x) / self.zoom
        pos.y = (pos.y - self.posistion.y) / self.zoom

        return pos

    def world_to_screen(self, pos):
        # convert a world posistion to a screen posistion
        return (pos - self.posistion) * self.zoom

    def modify_zoom(self, delta):
        # zoom into the center of the screen
        self.zoom += delta
