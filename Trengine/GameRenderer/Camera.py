from pyautogui import PRIMARY
import pygame


class Camera:

    def __init__(self, width, height, camera_min_x, camera_min_y, camera_max_x=10000000, camera_max_y=10000000):
        """
        Initialize the camera with the given parameters.

        Parameters:
        width (int): The width of the camera's view.
        height (int): The height of the camera's view.
        camera_min_x (int): The minimum x coordinate that the camera can move to.
        camera_min_y (int): The minimum y coordinate that the camera can move to.
        camera_max_x (int): The maximum x coordinate that the camera can move to. Defaults to 10000000.
        camera_max_y (int): The maximum y coordinate that the camera can move to. Defaults to 10000000.
        """
        self.width = width
        self.height = height
        # Set the camera's position to (0, 0) initially.
        self.posistion = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.zoom = 1  # Set the camera's initial zoom level to 1.
        self.rect = pygame.Rect(
            self.posistion.x, self.posistion.y, width, height)
        self.camera_min_y = camera_min_y
        self.camera_max_y = camera_max_y
        self.camera_min_x = camera_min_x
        self.camera_max_x = camera_max_x
        self.camera_rotation = 0

    def update(self):
        """
        Update the camera's state. This method should be called every frame.
        """
        if self.zoom < 0.5:
            self.zoom = 0.5
        # Set the camera's old position to its current position.
        self.old_posistion = self.posistion

    def move(self, delta):
        """
        Move the camera by the given delta vector.

        Parameters:
        delta (pygame.Vector2): The vector representing the amount to move the camera by.
        """
        self.posistion += delta  # Update the camera's position by adding the delta vector.

    def screen_to_world(self, pos):
        """
        Convert a screen position to a world position.

        Parameters:
        pos (pygame.Vector2): The position on the screen to convert.

        Returns:
        pygame.Vector2: The position in world coordinates.
        """
        pos = pygame.Vector2(pos)
        # Adjust for the camera's position and zoom level.
        pos.x = (pos.x - self.posistion.x) / self.zoom
        pos.y = (pos.y - self.posistion.y) / self.zoom
        return pos

    def world_to_screen(self, pos):
        """
        Convert a world position to a screen position.

        Parameters:
        pos (pygame.Vector2): The position in the world to convert.

        Returns:
        pygame.Vector2: The position on the screen.
        """
        return (pos - self.posistion) * self.zoom  # Adjust for the camera's position and zoom level.

    def modify_zoom(self, delta):
        """
        Modify the camera's zoom level by the given delta value.

        Parameters:
        delta (float): The amount to adjust the camera's zoom level by.
        """
        self.zoom += delta  # Update the camera's zoom level by adding the delta value.
        if self.zoom < 0.5:
            self.zoom = 0.5  # Ensure the zoom level doesn't go below 0.5.
