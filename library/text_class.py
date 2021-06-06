#from pygame import font, Surface, Rect
import pygame.font
import pygame.surface
import pygame.rect
from library.window_class import *
class Text(object):
    def __init__(self, X_Y, text, Text_Size = 30,  Color = [0,0,0]):
        self.X_Y = X_Y
        self.text = str(text)
        self.Text_Size = Text_Size
        self.Color = Color
        pygame.font.init()
        self.font = "georgia"
        self.surface = pygame.font.SysFont(self.font, self.Text_Size).render(self.text, True, self.Color)
        self.state = True
    
    def Draw(self, *args):
        if args:
            args[0].blit(self.surface, (self.X_Y[0], self.X_Y[1]))
        else:
            Window.surface.blit(self.surface, (self.X_Y[0], self.X_Y[1]))
            
    def Check(self, *args):
        if self.state:
            self.Update(self.text)
            self.state = False

    def Update(self, text):
        self.text = text
        self.surface = pygame.font.SysFont(self.font, self.Text_Size).render(str(self.text),  True, self.Color)
        self.rect = pygame.Rect((self.X_Y[0], self.X_Y[1], pygame.Surface.get_width(self.surface) + 3, pygame.Surface.get_height(self.surface) + 3))
        self.Draw()
        self.state = True
        
        return True
    