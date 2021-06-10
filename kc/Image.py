from pygame import image, KMOD_LALT, KMOD_NONE
import pygame.key
class Image(object):
    def __init__(self, X_Y_W_H, path, initial_scale, Moveable = False, img_pos = [0, 0]):
        self.image_surface = image.load(path)
        self.image_surface_scaled = self.image_surface.copy()
        self.image_surface_copy = self.image_surface.copy()
        self.X_Y_W_H = X_Y_W_H
        self.path = path
        self.Moveable = Moveable
        self.Move = False
        self.Surface = pygame.Surface([X_Y_W_H[2], X_Y_W_H[3]])
        self.img_pos = img_pos
        self.marker_image = pygame.image.load("img/marker.png")
        self.marker_W_H = [pygame.Surface.get_width(self.marker_image), pygame.Surface.get_height(self.marker_image)]
        self.markers_surfaces = []
        self.markers_rects = []
        self.markers_positions = []
        self.isMask = False
        self.Mask_Surface = pygame.Surface([pygame.Surface.get_width(self.image_surface), pygame.Surface.get_height(self.image_surface)])
        self.Mask_Surface_Copy = self.Mask_Surface.copy()
        scale_gen = 1
        self.Scales = [initial_scale]
        while 1:
            scale_gen = scale_gen * 2
            scaled_image =  pygame.transform.scale(self.image_surface, [int(self.image_surface.get_width() / scale_gen), int(self.image_surface.get_height()/ scale_gen)])
            if self.X_Y_W_H[2] < scaled_image.get_width() or self.X_Y_W_H[3] < scaled_image.get_height():
                self.Scales.append( float(self.Scales[0] * scale_gen) )
            else:
                break
        print(self.Scales)
        self.Scale_Pointer = 0
        self.Current_Scale = self.Scales[self.Scale_Pointer]
    
    def Calculate_Centered_Position(self):
        x = 0
        y = 0
        for i in range(len(self.markers_positions)):
            x += self.markers_positions[i][0]
            y += self.markers_positions[i][1]
        x = int( x / len(self.markers_positions))
        y = int( y / len(self.markers_positions))

        return [int(self.X_Y_W_H[0] / 2) - int(x / 2), int(self.X_Y_W_H[1] / 2) - int(y / 2)]

    def ZoomIn(self):
        if self.Scale_Pointer > 0:
            self.Scale_Pointer -= 1
            self.Current_Scale = self.Scales[self.Scale_Pointer]
            scale_gen = int(self.Scales[self.Scale_Pointer] / self.Scales[0])
            self.image_surface_scaled = pygame.transform.scale(self.image_surface, 
                                                            [int(self.image_surface.get_width() / scale_gen), int(self.image_surface.get_height()/ scale_gen)])
            self.image_surface_copy = self.image_surface_scaled.copy()
            self.Update_Markers(0, 0, 2)
            for i in range(len(self.markers_positions)):
                self.markers_positions[i][0] = self.markers_positions[i][0] * 2
                self.markers_positions[i][1] = self.markers_positions[i][1] * 2
            #if len(self.markers_positions) > 0:
            #    self.img_pos = self.Calculate_Centered_Position()
            #else:
            #    self.img_pos = [0, 0]
            self.img_pos[0] = int(self.img_pos[0] * 2)
            self.img_pos[1] = int(self.img_pos[1] * 2)
    def ZoomOut(self):
        if self.Scale_Pointer < len(self.Scales) - 1:
            self.Scale_Pointer += 1
            self.Current_Scale = self.Scales[self.Scale_Pointer]
            scale_gen = int(self.Scales[self.Scale_Pointer] / self.Scales[0])
            self.image_surface_scaled = pygame.transform.scale(self.image_surface, 
                                                            [int(self.image_surface.get_width() / scale_gen), int(self.image_surface.get_height()/ scale_gen)])
            self.image_surface_copy = self.image_surface_scaled.copy()
            self.Update_Markers(0, 0, 0.5)
            for i in range(len(self.markers_positions)):
                self.markers_positions[i][0] = int(self.markers_positions[i][0] / 2)
                self.markers_positions[i][1] = int(self.markers_positions[i][1] / 2)
            #if len(self.markers_positions) > 0:
            #    self.img_pos = self.Calculate_Centered_Position()
            #else:
            #    self.img_pos = [0, 0]
            self.img_pos[0] = int(self.img_pos[0] / 2)
            self.img_pos[1] = int(self.img_pos[1] / 2)

    def AddMarker(self, location):
        self.image_surface_copy = self.image_surface_scaled.copy()
        self.markers_positions.append([location[0] - int(self.marker_W_H[0] / 2), location[1] - int(self.marker_W_H[1] / 2) ])
        self.markers_surfaces.append(self.marker_image.copy())
        self.markers_rects.append(pygame.Rect([location[0] + self.X_Y_W_H[0] + self.img_pos[0] - int(self.marker_W_H[0] / 2), location[1] + self.X_Y_W_H[1]+ self.img_pos[1] - int(self.marker_W_H[1] / 2), pygame.Surface.get_width(pygame.image.load("img/marker.png")), pygame.Surface.get_height(pygame.image.load("img/marker.png"))]))
        return
    
    def DeleteMarker(self, i):
        self.markers_surfaces.pop(i)
        self.markers_rects.pop(i)
        self.markers_positions.pop(i)
        self.image_surface_copy = self.image_surface_scaled.copy()
    
    def DeleteAllMarkers(self):
        self.markers_surfaces = []
        self.markers_rects = []
        self.markers_positions = []
        self.image_surface_copy = self.image_surface_scaled.copy()
        
    def Debug(self):
        print(self.markers_positions)

    def Toggle_Mask(self):
        self.isMask = not(self.isMask)

    def Create_Mask(self):
        try:
            self.Mask_Surface_Copy = self.Mask_Surface.copy()
            #positions = self.markers_positions.copy()
            #for i in range(len(positions)):
            #    positions[i][0] = int(positions[i][0] / int(self.Scales[self.Scale_Pointer] / self.Scales[0]))
            #    positions[i][1] = int(positions[i][1] / int(self.Scales[self.Scale_Pointer] / self.Scales[0]))
            pygame.draw.polygon(self.Mask_Surface_Copy, [255, 0, 0], self.markers_positions)
            self.Mask_Surface_Copy.set_colorkey([0, 0, 0])
            a = pygame.mask.from_surface(self.Mask_Surface_Copy)
            
            print(float(a.count() * float(self.Scales[self.Scale_Pointer]*self.Scales[self.Scale_Pointer])))
            a.invert()
            b = a.to_surface()
            b.set_colorkey([0, 0, 0])
            self.Mask_Surface_Copy = self.image_surface_scaled.copy()
            self.Mask_Surface_Copy.blit(b, [0, 0])
            #self.Mask_Surface_Copy = pygame.Surface([pygame.Surface.get_width(self.image_surface), pygame.Surface.get_height(self.image_surface)], masks = a)#a.to_surface()
            return True
        except:
            return False
        

    def Draw(self):
        self.Surface.fill([230, 230, 230])
        if len(self.markers_positions) > 2:
            for i in range(len(self.markers_positions) - 1):
                pygame.draw.aaline(
                    self.image_surface_copy, 
                    [255, 255, 255], 
                    [self.markers_positions[i][0] + int(self.marker_W_H[0] / 2), self.markers_positions[i][1] + int(self.marker_W_H[1] / 2)], 
                    [self.markers_positions[i + 1][0] + int(self.marker_W_H[0] / 2), self.markers_positions[i + 1][1] + int(self.marker_W_H[1] / 2)], 2)
            pygame.draw.aaline(self.image_surface_copy, [255, 255, 255], [self.markers_positions[0][0] + int(self.marker_W_H[0] / 2), self.markers_positions[0][1] + int(self.marker_W_H[1] / 2)], [self.markers_positions[-1][0] + int(self.marker_W_H[0] / 2), self.markers_positions[-1][1] + int(self.marker_W_H[1] / 2)], 2)
            #pygame.draw.lines(self.image_surface_copy, [255, 255, 255], True, self.markers_positions)
        for i in range(len(self.markers_surfaces)):
            self.image_surface_copy.blit(self.markers_surfaces[i], [self.markers_positions[i][0], self.markers_positions[i][1]])
        if self.isMask:
            #self.image_surface_copy.blit(self.Mask_Surface_Copy, [0, 0])
            self.Surface.blit(self.Mask_Surface_Copy, self.img_pos)
        else:
            self.Surface.blit(self.image_surface_copy, self.img_pos)
        
        return self.Surface

    def Toggle_Movement(self):
        self.Moveable = not(self.Moveable)

    def Update_Markers(self, x = 0, y = 0, mult = 1):
        for i in range(len(self.markers_rects)):
            self.markers_rects[i] = pygame.Rect((mult * (self.markers_rects[i][0] + x), mult * (self.markers_rects[i][1] + y), self.markers_rects[i][2], self.markers_rects[i][3]))


    def Check(self, Event):
        result = False
        if self.Moveable:
            if Event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(self.X_Y_W_H).collidepoint(Event.pos):
                    if Event.button == 3:
                        self.Move = True
                    if Event.button == 1:
                        for i in range(len(self.markers_surfaces)):
                            if pygame.Rect(self.markers_rects[i]).collidepoint(Event.pos):
                                self.DeleteMarker(i)
                                print("Marker deleted")
                                result = "Deleted"
                                return True
                        if result != "Deleted":
                            self.AddMarker([Event.pos[0] - self.X_Y_W_H[0] - self.img_pos[0], Event.pos[1] - self.X_Y_W_H[1] - self.img_pos[1]])
                            print("Marker added")
                            return True
            if Event.type == pygame.MOUSEBUTTONUP:
                if Event.button == 3:
                    self.Move = False
            if self.Move:
                if Event.type == pygame.MOUSEMOTION:
                    self.img_pos[0] += Event.rel[0]
                    self.img_pos[1] += Event.rel[1]
                    self.Update_Markers(Event.rel[0], Event.rel[1])
                    self.Draw()
            return True
