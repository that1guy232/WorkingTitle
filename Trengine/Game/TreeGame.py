import pygame


from Trengine.GameRenderer.Camera import Camera
from Trengine.GameRenderer.Renderer import Renderer


class TreeGame():
    def __init__(self) -> None:

        # Initialize pygame
        pygame.init()
        pygame.font.init()
        # display
        pygame.display.set_mode((800, 600))

        self.screen = pygame.display.get_surface()

        self.game_clock = pygame.time.Clock()
        self.running = True

        self.current_scene = None

        self.scenes = []

        self.events = []

        # default camera & renderer
        #    def __init__(self, width, height, camera_min_x, camera_min_y, camera_max_x=10000000, camera_max_y=10000000):
        self.camera = Camera(800, 600, 0, 0)

        pass

    def add_scene(self, scene):
        self.scenes.append(scene)
        pass

    def transition_to_scene(self, scene_name):
        found_scene = False
        for scene in self.scenes:
            if scene.name == scene_name:
                # on & off events
                scene.on_enter()
                self.current_scene.on_exit()
                self.current_scene = scene

                found_scene = True

        if not found_scene:

            # if we didn't find the scene, print an error and ex
            print("ERROR: Scene not found")
            # what scene are we looking for?
            print("Looking for scene: " + scene_name)
            # what scenes do we have?
            print("Available scenes:")
            for scene in self.scenes:
                print(scene.name)
            exit()

        pass

    def run(self):
        while self.running:
            dt = self.game_clock.get_time()
            self.current_scene.update(dt)
            self.current_scene.draw()
            self.game_clock.tick(60)

            # handle the exit event
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False
                    pass

                pass

                # handle the event
                self.current_scene.handle_event(event)

            pass

            # update the display
            pygame.display.flip()
        pass

    pass
