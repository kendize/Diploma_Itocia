import pygame.rect
import pygame.draw
import pygame.key
from kc.text_class import *
class Button(object):
    def __init__(
        self, 
        X_Y_W_H,
        text = "GUI",
        Text_Size = 30,
        Disabled_Text_Color = [0, 0, 0],
        Disabled_Body_Color = [255, 255, 255],
        Disabled_Border_Color = [0, 0, 0],
        Border_Size = 1,
        Enabled_Text_Color = [0, 0, 0],
        Enabled_Body_Color = [255, 255, 255],
        Enabled_Border_Color = [150, 0, 0],
        Centered = True,
        Switch = False,
        position = False
        ):

        self.X_Y_W_H = X_Y_W_H

        self.position = position
        self.Switch = Switch        # Changing type of button (is it switchable or just activated when clicked)
        self.Centered = Centered    # If Centered, then Text on Button will be centered, but not images, they always centered

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

        if self.text[0] == "/":                                                                             # If Text on button starts with "/", then program think that this Text is path for image
            self.img = pygame.image.load(self.text[1:])                                                     # Loading this image
            path = list(self.text)
            path.insert(-4, "!")
            path = ''.join(path)
            try:
                self.img2 = pygame.image.load(path[1:])
            except:
                self.img2 = self.img     
            self.X_Y_W_H[3] = pygame.Surface.get_height(self.img)
            self.X_Y_W_H[2] = pygame.Surface.get_width(self.img)
            self.surface = self.img.copy()
        else:                                                                                               # At this point program think that it's also text on button
            if pygame.Surface.get_height(self.Enabled_Text.surface) > self.X_Y_W_H[3]:                      # If height of Text surface is larger than the height of the button itself:
                self.X_Y_W_H[3] = pygame.Surface.get_height(self.Enabled_Text.surface) + 3                  # Resize Button to the height of Text Surface
            if pygame.Surface.get_width(self.Enabled_Text.surface) > self.X_Y_W_H[2]:                       # If width of Text surface is larger than the width of the button itself:
                self.X_Y_W_H[2] = pygame.Surface.get_width(self.Enabled_Text.surface)                       # Resize Button to the width of Text Surface
            self.surface = pygame.Surface((self.X_Y_W_H[2], self.X_Y_W_H[3]))
            self.surface.fill((self.Disabled_Body_Color))
        
        if self.Centered:                                                                                   # If Centered, then Text on Button will be centered, but not images, they always centered
            self.Text_X_Y = [
                int(self.X_Y_W_H[2]/2) - int(pygame.Surface.get_width(self.Enabled_Text.surface)/2),
                int(self.X_Y_W_H[3]/2) - int(pygame.Surface.get_height(self.Enabled_Text.surface)/2)]
        else:
            self.Text_X_Y = [0, 0]

        self.Enabled_Text = Text((self.Text_X_Y[0], self.Text_X_Y[1]), self.text, self.Text_Size, self.Enabled_Text_Color)
        self.Disabled_Text = Text((self.Text_X_Y[0], self.Text_X_Y[1]), self.text, self.Text_Size, self.Disabled_Text_Color)

        


        
        self.Active = False
        if not(self.position):                                                                                                          # Position variable is created for pseudo windows, i guess they will be removed in later versions
            self.rect = pygame.Rect((self.X_Y_W_H[0], self.X_Y_W_H[1], self.X_Y_W_H[2], self.X_Y_W_H[3]))                               # If not Position, then create rectangle with usual parameters
        else:                                                                                                                           # Else Change position of the rectangle according to pseudo window
            self.rect = pygame.Rect((self.X_Y_W_H[0] + position[0], self.X_Y_W_H[1] + position[1], self.X_Y_W_H[2], self.X_Y_W_H[3]))


    def Draw(self):
        self.Enabled_Text.text = self.text
        self.Disabled_Text.text = self.text
        self.surface.fill((self.Disabled_Body_Color))

        if self.Active:
            pygame.draw.rect(self.surface, self.Enabled_Body_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), 0)

            if self.Border_Size:
                pygame.draw.rect(self.surface, self.Enabled_Border_Color, (0, 0, self.X_Y_W_H[2] - 1, self.X_Y_W_H[3] - 1), self.Border_Size + 1) 
            if not(self.text[0] == "/"):  
                self.Enabled_Text.Draw(self.surface)
            else:
                self.surface = self.img.copy()
                self.surface.blit(self.img, (pygame.Surface.get_width(self.surface)/2 - pygame.Surface.get_width(self.img)/2, pygame.Surface.get_height(self.surface)/2 - pygame.Surface.get_height(self.img)/2))
            return self.surface

        elif not(self.Active):
            pygame.draw.rect(self.surface, self.Disabled_Body_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), 0)
            if self.Border_Size:
                pygame.draw.rect(self.surface, self.Disabled_Border_Color, (0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]), self.Border_Size)  
            if not(self.text[0] == "/"):   
                self.Disabled_Text.Draw(self.surface)
            else:
                self.surface = self.img2.copy()
                self.surface.blit(self.img2, (pygame.Surface.get_width(self.surface)/2 - pygame.Surface.get_width(self.img2)/2, pygame.Surface.get_height(self.surface)/2 - pygame.Surface.get_height(self.img2)/2))

            return self.surface


    def Check(self, Event):
        if not(self.Switch):
            if Event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(Event.pos):
                    if Event.button == 1:
                        self.Active = True
                        return False

            if Event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(Event.pos):
                    if Event.button == 1:
                        self.Active = False
                        return True
                else:
                    if Event.button == 1:
                        self.Active = False
                        return False
            return False

        else:
            if Event.type == pygame.MOUSEBUTTONDOWN:
                if Event.button == 1:
                    if self.rect.collidepoint(Event.pos):
                        self.Active = not(self.Active)
                        if not(self.Active):
                            return True
                        return False
                    else:
                        self.Active = False
                        return False
                    #else:
                    #    self.Active = False
                    #    return False
