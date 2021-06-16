import pygame.font
import pygame.surface
import pygame.rect

class Text(object):
    def __init__(self, X_Y_W_H, text, Text_Size = 30,  Color = [0,0,0], position = False, rwidth = 100000):
        self.X_Y_W_H = X_Y_W_H
        self.text = str(text)
        self.Text_Size = Text_Size
        self.Color = Color
        pygame.font.init()
        self.font = "georgia"
        self.rwidth = rwidth
        self.Render(self.text)
        
    
    def Draw(self, *args):
        self.rect = pygame.Rect((self.X_Y_W_H[0], self.X_Y_W_H[1], pygame.Surface.get_width(self.surface) + 3, pygame.Surface.get_height(self.surface) + 3))
        if args:
            args[0].blit(self.surface, (self.X_Y_W_H[0], self.X_Y_W_H[1]))
        else:
            return self.surface
    
    def Render(self, new_text):
        self.text = new_text
        
        while 1:
            self.surface = pygame.font.SysFont(self.font, self.Text_Size).render(str(self.text),  True, self.Color)
            if pygame.Surface.get_width(self.surface) > self.rwidth:
                self.Text_Size -= 2
            else:
                self.rect = pygame.Rect((self.X_Y_W_H[0], self.X_Y_W_H[1], pygame.Surface.get_width(self.surface) + 3, pygame.Surface.get_height(self.surface) + 3))
                break
        

    
