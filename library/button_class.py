#from pygame import Rect, draw, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import pygame.rect
import pygame.draw
import pygame.key
from library.text_class import *
class Button(object):
    def __init__(self, X_Y_W_H, text = "GUI", Text_Size = 30, Disabled_Text_Color = [0, 0, 0], Disabled_Body_Color = [255, 255, 255], Disabled_Border_Color = [0, 0, 0], Border_Size = 1, Enabled_Text_Color = [0, 0, 0], Enabled_Body_Color = [255, 255, 255], Enabled_Border_Color = [150, 0, 0], Centered = True, Switch = False):
        self.X_Y_W_H = X_Y_W_H

        self.Switch = Switch
        self.Centered = Centered

        self.Disabled_Body_Color = Disabled_Body_Color
        self.Disabled_Border_Color = Disabled_Border_Color
        self.Disabled_Text_Color = Disabled_Text_Color

        self.Enabled_Body_Color = Enabled_Body_Color
        self.Enabled_Border_Color = Enabled_Border_Color
        self.Enabled_Text_Color = Enabled_Text_Color

        self.Border_Size = Border_Size
        self.text = str(text)
        self.Text_Size = Text_Size

        self.Enabled_Text = Text((0, 0), self.text, self.Text_Size, self.Enabled_Text_Color)
        self.Disabled_Text = Text((0, 0), self.text, self.Text_Size, self.Disabled_Text_Color)

        if pygame.Surface.get_height(self.Enabled_Text.surface) > self.X_Y_W_H[3]:
            self.X_Y_W_H[3] = pygame.Surface.get_height(self.Enabled_Text.surface) + 3
        if pygame.Surface.get_width(self.Enabled_Text.surface) > self.X_Y_W_H[2]:
            self.X_Y_W_H[2] = pygame.Surface.get_width(self.Enabled_Text.surface)
            
        if self.Centered:
            self.Text_X_Y = [
                int(self.X_Y_W_H[2]/2) - int(pygame.Surface.get_width(self.Enabled_Text.surface)/2),
                int(self.X_Y_W_H[3]/2) - int(pygame.Surface.get_height(self.Enabled_Text.surface)/2)]
        else:
            self.Text_X_Y = [0, 0]

        self.Enabled_Text = Text((self.Text_X_Y[0], self.Text_X_Y[1]), self.text, self.Text_Size, self.Enabled_Text_Color)
        self.Disabled_Text = Text((self.Text_X_Y[0], self.Text_X_Y[1]), self.text, self.Text_Size, self.Disabled_Text_Color)

        

        self.surface = pygame.Surface((self.X_Y_W_H[2], self.X_Y_W_H[3]))
        self.surface.fill((self.Disabled_Body_Color))
        self.Active = False
        self.rect = pygame.Rect((self.X_Y_W_H[0], self.X_Y_W_H[1], self.X_Y_W_H[2], self.X_Y_W_H[3]))


    def Draw(self):
        self.Enabled_Text.text = self.text
        self.Disabled_Text.text = self.text
        self.surface.fill((self.Disabled_Body_Color))

        if self.Active:
            pygame.draw.rect(self.surface, self.Enabled_Body_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), 0)

            if self.Border_Size:
                pygame.draw.rect(self.surface, self.Enabled_Border_Color, (0, 0, self.X_Y_W_H[2] - 1, self.X_Y_W_H[3] - 1), self.Border_Size + 1)   
            self.Enabled_Text.Draw(self.surface)
            Window.surface.blit(self.surface, (self.X_Y_W_H[0], self.X_Y_W_H[1]))

        elif not(self.Active):
            pygame.draw.rect(self.surface, self.Disabled_Body_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), 0)
            if self.Border_Size:
                pygame.draw.rect(self.surface, self.Disabled_Border_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), self.Border_Size)   
            self.Disabled_Text.Draw(self.surface)
            Window.surface.blit(self.surface, (self.X_Y_W_H[0], self.X_Y_W_H[1]))


    def Check(self, Event):
        if not(self.Switch):
            if Event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(Event.pos):
                    if Event.button == 1:
                        self.Active = True
                        self.Draw()
                        return True

            if Event.type == pygame.MOUSEBUTTONUP:
                if Event.button == 1:
                    self.Active = False
                    self.Draw()
                    return False
            return False
        else:
            if Event.type == pygame.MOUSEBUTTONDOWN:
                if Event.button == 1:
                    if self.rect.collidepoint(Event.pos):
                        self.Active = not(self.Active)
                        self.Draw()
                        if not(self.Active):
                            self.Draw()
                            return True
                        return False
                    else:
                        self.Active = False
                        self.Draw()
                        return False
