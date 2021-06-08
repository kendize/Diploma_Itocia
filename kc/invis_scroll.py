import pygame.key
class Invis_Scroll(object):
    def __init__(self, y):
        self.y = y
        self.X_Y_W_H = [0, 0, 1, 1]
        self.surface = pygame.Surface((self.X_Y_W_H[2], self.X_Y_W_H[3]))

    def Check(self, Event):
        if Event.type == pygame.MOUSEBUTTONDOWN:
            if Event.button == 4:
                self.y = 20
                return True
            if Event.button == 5:
                self.y = -20
                return True
    def Draw(self):
        return self.surface
