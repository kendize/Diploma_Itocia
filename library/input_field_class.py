#from pygame import Rect, draw, MOUSEBUTTONDOWN, KEYDOWN, K_BACKSPACE, K_RETURN
import pygame.rect
import pygame.draw
import pygame.key
from library.text_class import *
class Input_Field(object):
    def __init__(self, X_Y_W_H, text = "GUI", Text_Size = 30, Disabled_Text_Color = [0, 0, 0], Disabled_Body_Color = [255, 255, 255], Disabled_Border_Color = [0, 0, 0], Border_Size = 1, Enabled_Text_Color = [0, 0, 0], Enabled_Body_Color = [255, 255, 255], Enabled_Border_Color = [150, 0, 0]):
        self.X_Y_W_H = X_Y_W_H

        self.Disabled_Body_Color = Disabled_Body_Color
        self.Disabled_Border_Color = Disabled_Border_Color
        self.Disabled_Text_Color = Disabled_Text_Color

        self.Enabled_Body_Color = Enabled_Body_Color
        self.Enabled_Border_Color = Enabled_Border_Color
        self.Enabled_Text_Color = Enabled_Text_Color

        self.Border_Size = Border_Size
        self.text = text
        self.Text_Size = Text_Size
        self.Enabled_Text = Text((1, 1), self.text, self.Text_Size, self.Enabled_Text_Color)
        self.Disabled_Text = Text((1, 1), self.text, self.Text_Size, self.Disabled_Text_Color)

        if pygame.Surface.get_height(self.Enabled_Text.surface) > self.X_Y_W_H[3]:
            self.X_Y_W_H[3] = pygame.Surface.get_height(self.Enabled_Text.surface) + 3
        if pygame.Surface.get_width(self.Enabled_Text.surface) > self.X_Y_W_H[2]:
            self.X_Y_W_H[2] = pygame.Surface.get_width(self.Enabled_Text.surface)

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
                pygame.draw.rect(self.surface, self.Enabled_Border_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), self.Border_Size)   
            self.Enabled_Text.Draw(self.surface)
            Window.surface.blit(self.surface, (self.X_Y_W_H[0], self.X_Y_W_H[1]))

        elif not(self.Active):
            pygame.draw.rect(self.surface, self.Disabled_Body_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), 0)
            if self.Border_Size:
                pygame.draw.rect(self.surface, self.Disabled_Border_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), self.Border_Size)   
            self.Disabled_Text.Draw(self.surface)
            Window.surface.blit(self.surface, (self.X_Y_W_H[0], self.X_Y_W_H[1]))

    def Check(self, Event):
        if Event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(Event.pos):
                if Event.button == 1:
                    self.Active = not(self.Active)
                    self.Draw()
                    return True

        if self.Active:
            if Event.type == pygame.MOUSEBUTTONDOWN:
                if Event.button == 1:
                    self.Active = False
                    self.Draw()
                    return False
            if Event.type == pygame.KEYDOWN:
                # Erasing last letter from (text) variable
                if Event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                    # Drawing
                    self.Draw()
                    return True

                # Disable input field if was pressed [Enter] key 
                elif Event.key == pygame.K_RETURN:
                    self.Active = False
                    self.Draw()
                    return True

                # In other cases check for unicode of pressed key and append it in (self.text) variable
                else:
                    self.text += Event.unicode
                    self.Enabled_Text.text = self.text
                    self.Disabled_Text.text = self.text

                    # Drawing
                    self.Draw()
                    return True
        return False

