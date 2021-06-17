from pygame import image, KMOD_LALT, KMOD_NONE
import pygame.key
class Image_Manipulator(object):
    def __init__(self, X_Y_W_H, path, initial_scale, img_pos = [0, 0]):
        self.image_surface = image.load(path)
        self.image_surface_scaled = self.image_surface.copy()
        self.image_surface_copy = self.image_surface.copy()
        self.X_Y_W_H = X_Y_W_H
        self.path = path
        self.Move = False
        self.Surface = pygame.Surface([X_Y_W_H[2], X_Y_W_H[3]])
        self.img_pos = [0, 0]
        self.marker_image = pygame.image.load("img/marker.png")
        self.marker_W_H = [pygame.Surface.get_width(self.marker_image), pygame.Surface.get_height(self.marker_image)]
        self.markers_surfaces = []
        self.markers_rects = []
        self.markers_rects = []
        self.markers_positions = []
        self.scaled_markers_positions = []
        self.isMask = False
        self.Mask_Surface = pygame.Surface([pygame.Surface.get_width(self.image_surface), pygame.Surface.get_height(self.image_surface)])
        self.Mask_Surface_Copy = self.Mask_Surface.copy()
        self.Result_Surface = False
        scale_gen = 1
        self.initial_scale = float(initial_scale)
        self.Scales = [self.initial_scale]
        self.Colors = []
        while 1:
            scale_gen = scale_gen * 2
            scaled_image =  pygame.transform.scale(self.image_surface, [int(self.image_surface.get_width() / scale_gen), int(self.image_surface.get_height()/ scale_gen)])
            if self.X_Y_W_H[2] < scaled_image.get_width() or self.X_Y_W_H[3] < scaled_image.get_height():
                self.Scales.append( float(self.Scales[0] * scale_gen) )
            else:
                self.Scales.append( float(self.Scales[0] * scale_gen) )
                break
        print(self.Scales)
        self.Scale_Pointer = 0
        self.Current_Scale = self.Scales[self.Scale_Pointer]
    
    def Calculate_Centered_Position(self):
        x = 0
        y = 0
        for i in range(len(self.scaled_markers_positions)):
            x += self.scaled_markers_positions[i][0]
            y += self.scaled_markers_positions[i][1]
        x = int( x / len(self.scaled_markers_positions))
        y = int( y / len(self.scaled_markers_positions))

        return [x, y]

    def ZoomIn(self):
        if self.Scale_Pointer > 0:
            self.Scale_Pointer -= 1
            self.Current_Scale = self.Scales[self.Scale_Pointer]
            scale_gen = int(self.Scales[self.Scale_Pointer] / self.Scales[0])
            self.image_surface_scaled = pygame.transform.scale(self.image_surface, 
                                                            [int(self.image_surface.get_width() / scale_gen), int(self.image_surface.get_height()/ scale_gen)])
            self.image_surface_copy = self.image_surface_scaled.copy()
            
            for i in range(len(self.markers_positions)):
                self.scaled_markers_positions[i][0] = self.markers_positions[i][0] / scale_gen
                self.scaled_markers_positions[i][1] = self.markers_positions[i][1] / scale_gen
            if len(self.markers_positions) > 0:
                self.img_pos[0] = -int(self.Calculate_Centered_Position()[0]) + int(self.X_Y_W_H[2]/2)
                self.img_pos[1] = -int(self.Calculate_Centered_Position()[1]) + int(self.X_Y_W_H[3]/2)
            else:
                self.img_pos[0] = int(self.img_pos[0] / 2)
                self.img_pos[1] = int(self.img_pos[1] / 2)
            for i in range(len(self.markers_rects)):
                self.markers_rects[i] = pygame.Rect((int((self.markers_positions[i][0])/ scale_gen) + self.img_pos[0] + self.X_Y_W_H[0], int((self.markers_positions[i][1] )/ scale_gen) + self.img_pos[1] + self.X_Y_W_H[1], self.markers_rects[i][2], self.markers_rects[i][3]))



    def ZoomOut(self):
        if self.Scale_Pointer < len(self.Scales) - 1:
            self.Scale_Pointer += 1
            self.Current_Scale = self.Scales[self.Scale_Pointer]
            scale_gen = int(self.Scales[self.Scale_Pointer] / self.Scales[0])
            self.image_surface_scaled = pygame.transform.scale(self.image_surface, 
                                                            [int(self.image_surface.get_width() / scale_gen), int(self.image_surface.get_height()/ scale_gen)])
            self.image_surface_copy = self.image_surface_scaled.copy()
            
            for i in range(len(self.markers_positions)):
                self.scaled_markers_positions[i][0] = int(self.markers_positions[i][0] / scale_gen)
                self.scaled_markers_positions[i][1] = int(self.markers_positions[i][1] / scale_gen)

            if len(self.markers_positions) > 0:
                self.img_pos[0] = -int(self.Calculate_Centered_Position()[0]) + int(self.X_Y_W_H[2]/2)
                self.img_pos[1] = -int(self.Calculate_Centered_Position()[1]) + int(self.X_Y_W_H[3]/2)
            else:
                self.img_pos[0] = int(self.img_pos[0] / 2)
                self.img_pos[1] = int(self.img_pos[1] / 2)
            for i in range(len(self.markers_rects)):
                self.markers_rects[i] = pygame.Rect((int((self.markers_positions[i][0])/ scale_gen) + self.img_pos[0] + self.X_Y_W_H[0], int((self.markers_positions[i][1] )/ scale_gen) + self.img_pos[1] + self.X_Y_W_H[1], self.markers_rects[i][2], self.markers_rects[i][3]))


    def AddMarker(self, location):

        self.Current_Scale = self.Scales[self.Scale_Pointer]
        scale_gen = int(self.Scales[self.Scale_Pointer] / self.Scales[0])
        self.image_surface_copy = self.image_surface_scaled.copy()
        self.scaled_markers_positions.append([location[0] - int(self.marker_W_H[0] / 2), location[1] - int(self.marker_W_H[1] / 2) ])
        self.markers_positions.append([scale_gen * (location[0] - int(self.marker_W_H[0] / 2)), scale_gen * (location[1] - int(self.marker_W_H[1] / 2)) ])
        self.markers_surfaces.append(self.marker_image.copy())
        self.markers_rects.append(pygame.Rect([(location[0] + self.X_Y_W_H[0] + self.img_pos[0]) - int(self.marker_W_H[0] / 2), (location[1] + self.X_Y_W_H[1]+ self.img_pos[1]) - int(self.marker_W_H[1] / 2), pygame.Surface.get_width(pygame.image.load("img/marker.png")), pygame.Surface.get_height(pygame.image.load("img/marker.png"))]))
        return
    
    def DeleteMarker(self, i):
        if len(self.markers_positions) > 0:
            self.markers_surfaces.pop(i)
            self.markers_rects.pop(i)
            self.markers_positions.pop(i)
            self.scaled_markers_positions.pop(i)
            self.image_surface_copy = self.image_surface_scaled.copy()
    
    def DeleteAllMarkers(self):
        self.markers_surfaces = []
        self.markers_rects = []
        self.markers_positions = []
        self.scaled_markers_positions = []
        self.image_surface_copy = self.image_surface_scaled.copy()
        print("All markers deleted!")
        
    def Debug(self):
        print(self.markers_positions)

    def Toggle_Mask(self):
        self.isMask = not(self.isMask)

    def Calculate_Square(self):
        if len(self.markers_positions) > 2:
            Mask_Surface_Copy = self.Mask_Surface.copy()
            pygame.draw.polygon(Mask_Surface_Copy, [255, 0, 0], self.markers_positions)
            Mask_Surface_Copy .set_colorkey([0, 0, 0])
            a = pygame.mask.from_surface(Mask_Surface_Copy)
            result = float(a.count() * float(self.Scales[0]*self.Scales[0]))
        else:
            result = 0
        if result > 0 and result < 10000:
            result = str(round(result, 3)) + " м²"
        elif result >= 10000:
            result = str(round(float(result / 10000), 3) )+ " га"
        print(result)
        return result

    def Create_Mask(self):
        try:
            self.Mask_Surface_Copy = self.Mask_Surface.copy()
            pygame.draw.polygon(self.Mask_Surface_Copy, [255, 0, 0], self.markers_positions)
            self.Mask_Surface_Copy.set_colorkey([0, 0, 0])
            a = pygame.mask.from_surface(self.Mask_Surface_Copy)
            a.invert()
            b = a.to_surface()
            b.set_colorkey([0, 0, 0])
            self.Mask_Surface_Copy = self.image_surface.copy()
            self.Mask_Surface_Copy.blit(b, [0, 0])
            x = [i[0] for i in self.markers_positions]
            y = [i[1] for i in self.markers_positions]
            self.Result_Surface = pygame.Surface([max(x) - min(x), max(y) - min(y)])
            self.Result_Surface.convert()
            self.Result_Surface.blit(self.Mask_Surface_Copy, [0, 0], [min(x), min(y), max(x), max(y)])
            self.Result_Surface.set_colorkey([255, 255, 255])
            return True
        except:
            return False

    def Top_Colors(self):
        try:
            result = {}
            for x in range(self.Result_Surface.get_width()):
                for y in range(self.Result_Surface.get_height()):
                    a = str(self.Result_Surface.get_at([x, y])[0:-1])#######
                    result[a] = result.get(a, 0) + 1

            values = [i[1]  for i in result.items()]
            keys = [i[0]  for i in result.items()]

            index = keys.index("(255, 255, 255)")
            values.pop(index)
            keys.pop(index)
            result_values = []
            result_keys = []

            size = len(values)
            if size > 50:
                size = 50

            for i in range(size):
                index = values.index(max(values))
                result_values.append(str(values.pop(index)))
                result_keys.append(str(keys.pop(index)))
                #print(result_keys[i] + " --- " + result_values[i])
            self.Colors = [result_keys, result_values]
            return [result_keys, result_values]
        except:
            return False
        

    def Draw(self):
        self.Surface.fill([230, 220, 220])
        if len(self.markers_positions) > 2:
            for i in range(len(self.markers_positions) - 1):
                pygame.draw.line(
                    self.image_surface_copy, 
                    [255, 255, 255], 
                    [self.scaled_markers_positions[i][0] + int(self.marker_W_H[0] / 2), self.scaled_markers_positions[i][1] + int(self.marker_W_H[1] / 2)], 
                    [self.scaled_markers_positions[i + 1][0] + int(self.marker_W_H[0] / 2), self.scaled_markers_positions[i + 1][1] + int(self.marker_W_H[1] / 2)], 2)
            pygame.draw.line(self.image_surface_copy, [255, 255, 255], [self.scaled_markers_positions[0][0] + int(self.marker_W_H[0] / 2), self.scaled_markers_positions[0][1] + int(self.marker_W_H[1] / 2)], [self.scaled_markers_positions[-1][0] + int(self.marker_W_H[0] / 2), self.scaled_markers_positions[-1][1] + int(self.marker_W_H[1] / 2)], 2)
        for i in range(len(self.markers_surfaces)):
            self.image_surface_copy.blit(self.markers_surfaces[i], [self.scaled_markers_positions[i][0], self.scaled_markers_positions[i][1]])
        if self.isMask:
            self.Surface.blit(self.Result_Surface, self.img_pos)
        else:
            self.Surface.blit(self.image_surface_copy, self.img_pos)
        pygame.draw.rect(self.Surface, [255, 255, 255], [0, 0, self.X_Y_W_H[2], self.X_Y_W_H[3]], 2)
        return self.Surface

    def Update_Markers(self, x = 0, y = 0):
        for i in range(len(self.markers_rects)):
            self.markers_rects[i] = pygame.Rect((int((self.markers_rects[i][0] + x)), int((self.markers_rects[i][1] + y)), self.markers_rects[i][2], self.markers_rects[i][3]))


    def Check(self, Event):
        result = False
    
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
                        if pygame.Rect([self.img_pos[0] + self.X_Y_W_H[0], self.img_pos[1] + self.X_Y_W_H[1]], [self.image_surface_scaled.get_width(), self.image_surface_scaled.get_height()]).collidepoint(Event.pos):
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
