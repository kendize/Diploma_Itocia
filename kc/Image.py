from pygame import image

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
