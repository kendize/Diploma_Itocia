from pygame import FULLSCREEN, QUIT, RESIZABLE, NOFRAME
import pygame.display
import pygame.time
import os
class Window_Class(object):
    def __init__(self, window_width = 800, window_height = 600, window_caption = "Application", Body_Color = [255, 255, 255], fullscreen = False):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
        self.fullscreen = fullscreen
        self.width = window_width
        self.height = window_height
        self.caption = window_caption
        self.Body_Color = Body_Color
        self.surface = pygame.display.set_mode((self.width, self.height), RESIZABLE)

    def Start(self):
        pygame.init()
        if self.fullscreen:
            self.surface = pygame.display.set_mode((self.width, self.height), FULLSCREEN, RESIZABLE)
        else:
            self.surface = pygame.display.set_mode((self.width, self.height), NOFRAME ,RESIZABLE)
        pygame.display.set_caption(self.caption)
        self.surface.fill(self.Body_Color)
        pygame.display.update()
 
def Update(FPS):
    pygame.display.update()
    Clock.tick(FPS)

def Draw(subject, obj = False):
    surface = subject.Draw()
    if obj:
        obj.blit(surface, (subject.X_Y_W_H[0], subject.X_Y_W_H[1]))
    else:
        Window.surface.blit(surface, (subject.X_Y_W_H[0], subject.X_Y_W_H[1]))

Window = Window_Class(1, 1, "GUI")
Window.Start()
Clock = pygame.time.Clock()



