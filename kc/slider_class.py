import pygame.rect
import pygame.draw
import pygame.key
import pygame.surface
from pygame import MOUSEMOTION, MOUSEBUTTONUP
from math import fabs

class Slider(object):
    def __init__(self, X_Y_W_H, Tension = True, Slider_Color = [0, 255, 0], Path_Color = [0, 0, 255], Max_Value = 100, position = False):
        self.X_Y_W_H = X_Y_W_H
        self.position = position
        self.Slider_X_Y = [0, 0]
        self.Tension = Tension
        self.Slider_Color = Slider_Color
        self.Path_Color = Path_Color
        self.surface = pygame.Surface((self.X_Y_W_H[2], self.X_Y_W_H[3]))
        if not(self.position):
            self.rect = pygame.Rect((self.X_Y_W_H[0], self.X_Y_W_H[1], self.X_Y_W_H[2], self.X_Y_W_H[3]))
        else:
            self.rect = pygame.Rect((self.X_Y_W_H[0] + self.position[0], self.X_Y_W_H[1] + self.position[1], self.X_Y_W_H[2], self.X_Y_W_H[3]))
        self.Max_Value = Max_Value
        self.Value = 0

    def Draw(self):
        if self.Tension:
            pygame.draw.rect(self.surface, self.Path_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), 0)
            pygame.draw.rect(self.surface, self.Slider_Color, (self.Slider_X_Y[0], self.Slider_X_Y[1], self.X_Y_W_H[3], self.X_Y_W_H[3]), 0)
        else:
            pygame.draw.rect(self.surface, self.Path_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), 0)
            pygame.draw.rect(self.surface, self.Slider_Color, (self.Slider_X_Y[0], self.Slider_X_Y[1], self.X_Y_W_H[2], self.X_Y_W_H[2]), 0)
        return self.surface
    
    def Check(self, Event):
        if self.Tension:
            if Event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(Event.pos):
                    if Event.button == 1:
                        if not(self.position):
                            self.Slider_X_Y[0] = Event.pos[0] - self.X_Y_W_H[0] - self.X_Y_W_H[3]/2
                            if self.Slider_X_Y[0] > self.X_Y_W_H[2] - self.X_Y_W_H[3]:
                                self.Slider_X_Y[0] = self.X_Y_W_H[2] - self.X_Y_W_H[3]
                            if self.Slider_X_Y[0] < 0:
                                self.Slider_X_Y[0] = 0
                            self.Value = (self.Max_Value/(self.X_Y_W_H[2]-self.X_Y_W_H[3]))*self.Slider_X_Y[0]
                        else:
                            self.Slider_X_Y[0] = Event.pos[0] - self.X_Y_W_H[0] - self.X_Y_W_H[3]/2 - self.position[0]
                            if self.Slider_X_Y[0] > self.X_Y_W_H[2] - self.X_Y_W_H[3]:
                                self.Slider_X_Y[0] = self.X_Y_W_H[2] - self.X_Y_W_H[3]
                            if self.Slider_X_Y[0] < 0:
                                self.Slider_X_Y[0] = 0
                            self.Value = (self.Max_Value/(self.X_Y_W_H[2]-self.X_Y_W_H[3]))*self.Slider_X_Y[0]
                            return self.Value
            if Event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(Event.pos):
                    if Event.buttons[0] == 1:
                        self.Slider_X_Y[0] = Event.pos[0] - self.X_Y_W_H[0] - self.X_Y_W_H[3]/2 - self.position[0]
                        if self.Slider_X_Y[0] > self.X_Y_W_H[2] - self.X_Y_W_H[3]:
                            self.Slider_X_Y[0] = self.X_Y_W_H[2] - self.X_Y_W_H[3]
                        if self.Slider_X_Y[0] < 0:
                            self.Slider_X_Y[0] = 0
                        self.Value = (self.Max_Value/(self.X_Y_W_H[2]-self.X_Y_W_H[3]))*self.Slider_X_Y[0]
                        return self.Value
        else:

            if Event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(Event.pos):
                    if Event.button == 1:
                        if not(self.position):
                            self.Slider_X_Y[1] = Event.pos[1] - self.X_Y_W_H[1] - self.X_Y_W_H[2]/2
                            if self.Slider_X_Y[1] > self.X_Y_W_H[3] - self.X_Y_W_H[2]:
                                self.Slider_X_Y[0] = self.X_Y_W_H[3] - self.X_Y_W_H[2]
                            if self.Slider_X_Y[1] < 0:
                                self.Slider_X_Y[1] = 0
                            self.Value = (self.Max_Value/(self.X_Y_W_H[3]-self.X_Y_W_H[2]))*self.Slider_X_Y[1]
                            return self.Value
                        else:
                            self.Slider_X_Y[1] = Event.pos[1] - self.X_Y_W_H[1] - self.X_Y_W_H[2]/2  - self.position[1]
                            if self.Slider_X_Y[1] > self.X_Y_W_H[3] - self.X_Y_W_H[2]:
                                self.Slider_X_Y[1] = self.X_Y_W_H[3] - self.X_Y_W_H[2]
                            if self.Slider_X_Y[1] < 0:
                                self.Slider_X_Y[1] = 0
                            self.Value = (self.Max_Value/(self.X_Y_W_H[3]-self.X_Y_W_H[2]))*self.Slider_X_Y[1]
                            return self.Value
            if Event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(Event.pos):
                    if Event.buttons[0] == 1:
                        self.Slider_X_Y[1] = Event.pos[1] - self.X_Y_W_H[1] - self.X_Y_W_H[2]/2 - self.position[1]
                        if self.Slider_X_Y[1] > self.X_Y_W_H[3] - self.X_Y_W_H[2]:
                            self.Slider_X_Y[1] = self.X_Y_W_H[3] - self.X_Y_W_H[2]
                        if self.Slider_X_Y[1] < 0:
                            self.Slider_X_Y[1] = 0
                        self.Value = (self.Max_Value/(self.X_Y_W_H[3]-self.X_Y_W_H[2]))*self.Slider_X_Y[1]
                        return self.Value
        return False
