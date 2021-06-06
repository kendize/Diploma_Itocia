from pygame import FULLSCREEN, QUIT, RESIZABLE
import pygame.display
import pygame.time
class Window_Class(object):
    def __init__(self, window_width, window_height, window_caption, Body_Color = [255, 255, 255], fullscreen = False):
        self.fullscreen = fullscreen
        self.width = window_width
        self.height = window_height
        self.caption = window_caption
        self.Body_Color = Body_Color

    def Start(self):
        if self.fullscreen:
            self.surface = pygame.display.set_mode((self.width, self.height), FULLSCREEN, RESIZABLE)
        else:
            self.surface = pygame.display.set_mode((self.width, self.height), RESIZABLE)
        pygame.display.set_caption(self.caption)
        self.surface.fill(self.Body_Color)
        pygame.display.update()



Window = Window_Class(1, 1, "GUI")
Clock = pygame.time.Clock()

def Update(FPS):

    pygame.display.update()
    Clock.tick(FPS)