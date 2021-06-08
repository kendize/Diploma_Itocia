from pygame import image
import pygame.key
class Image(object):
    def __init__(self, X_Y, path, Moveable = False):
        self.surface = image.load(path)
        self.X_Y_W_H = [X_Y[0], X_Y[1], self.surface.get_width(), self.surface.get_height()]
        self.path = path
        self.Moveable = Moveable
        self.Move = False
        
    def Draw(self):
        return self.surface

    def Check(self, Event):
        if self.Moveable:
            if Event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(self.X_Y_W_H).collidepoint(Event.pos):
                    if Event.button == 3:
                        self.Move = True
            if Event.type == pygame.MOUSEBUTTONUP:
                if Event.button == 3:
                    self.Move = False
            if self.Move:
                if Event.type == pygame.MOUSEMOTION:
                    self.X_Y_W_H[0] += Event.rel[0]
                    self.X_Y_W_H[1] += Event.rel[1]
                    self.Draw()

class Animation(object):
    def __init__(self, number_of_frames, path, name, file_format, speed, FPS):
        self.number_of_frames = number_of_frames
        self.path = path
        self.name = name
        self.file_format = file_format
        self.list_of_surfaces = []
        self.FPS = FPS
        self.speed = speed
        self.Update_Speed(self.speed)
        self.Load_Animated_Frames(self.number_of_frames, self.path, self.name, self.file_format)
    
    def Update_Speed(self, speed):
        if speed > 0:
            self.FPF = self.FPS * (1/ speed) / self.number_of_frames
        self.speed = speed
        self.frame = 0
        self.counter = -1

    def Load_Animated_Frames(self, number_of_frames, path, name, file_format):
        self.list_of_surfaces = []
        for element in range(self.number_of_frames):
            self.list_of_surfaces.append(image.load((path + "/" + name + "-" + str(element) + "." + file_format)))

    def Draw(self, X_Y, surface):
        self.Update_Frame()
        surface.blit(self.list_of_surfaces[self.frame], (X_Y[0], X_Y[1]))

    def Update_Frame(self):
        if self.speed == 0:
            return 0

        self.counter += 1
        if self.counter >= self.FPF:
            self.counter = -1
            self.frame += 1
            if self.frame >= self.number_of_frames:
                self.frame = 0
