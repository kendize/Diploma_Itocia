import kc
from kc import *

class Box():
    def __init__(self,
    X_Y_W_H = [10, 10, 100, 100],
    Border_Size = 1,
    Body_Color = [230, 230, 230],
    Border_Color = [0, 0, 0]
    ):
        self.X_Y_W_H = X_Y_W_H
        self.Border_Size = Border_Size
        self.Body_Color = Body_Color
        self.Border_Color = Border_Color
        
        self.surface = kc.pygame.Surface((X_Y_W_H[2], X_Y_W_H[3]))

    def Draw(self):
        self.surface.fill(self.Body_Color)
        kc.pygame.draw.rect(self.surface, self.Border_Color, [0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]], self.Border_Size)
        return self.surface
