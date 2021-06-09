from pygame import image, KMOD_LALT, KMOD_NONE
import pygame.key
class Image(object):
    def __init__(self, X_Y_W_H, path, Moveable = False, img_pos = [0, 0]):
        self.image_surface = image.load(path)
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
        self.AddMarker([100, 100])

    
    def AddMarker(self, location):
        self.image_surface_copy = self.image_surface.copy()
        self.markers_positions.append([location[0] - int(self.marker_W_H[0] / 2), location[1] - int(self.marker_W_H[1] / 2) ])
        self.markers_surfaces.append(self.marker_image.copy())
        self.markers_rects.append(pygame.Rect([location[0] + self.X_Y_W_H[0] + self.img_pos[0] - int(self.marker_W_H[0] / 2), location[1] + self.X_Y_W_H[1]+ self.img_pos[1] - int(self.marker_W_H[1] / 2), pygame.Surface.get_width(pygame.image.load("img/marker.png")), pygame.Surface.get_height(pygame.image.load("img/marker.png"))]))
        return
    
    def DeleteMarker(self, i):
        self.markers_surfaces.pop(i)
        self.markers_rects.pop(i)
        self.markers_positions.pop(i)
        self.image_surface_copy = self.image_surface.copy()
    
    def DeleteAllMarkers(self):
        self.markers_surfaces = []
        self.markers_rects = []
        self.markers_positions = []
        self.image_surface_copy = self.image_surface.copy()
        

    def Draw(self):
        self.Surface.fill([230, 230, 230])
        if len(self.markers_positions) > 2:
            for i in range(len(self.markers_positions) - 1):
                pygame.draw.line(
                    self.image_surface_copy, 
                    [255, 255, 255], 
                    [self.markers_positions[i][0] + int(self.marker_W_H[0] / 2), self.markers_positions[i][1] + int(self.marker_W_H[1] / 2)], 
                    [self.markers_positions[i + 1][0] + int(self.marker_W_H[0] / 2), self.markers_positions[i + 1][1] + int(self.marker_W_H[1] / 2)], 2)
            pygame.draw.line(self.image_surface_copy, [255, 255, 255], [self.markers_positions[0][0] + int(self.marker_W_H[0] / 2), self.markers_positions[0][1] + int(self.marker_W_H[1] / 2)], [self.markers_positions[-1][0] + int(self.marker_W_H[0] / 2), self.markers_positions[-1][1] + int(self.marker_W_H[1] / 2)], 2)
            #pygame.draw.lines(self.image_surface_copy, [255, 255, 255], True, self.markers_positions)
        for i in range(len(self.markers_surfaces)):
            self.image_surface_copy.blit(self.markers_surfaces[i], [self.markers_positions[i][0], self.markers_positions[i][1]])#[self.img_pos[0] + self.markers_rects[i][0], self.img_pos[1] + self.markers_rects[i][1]] )
        self.Surface.blit(self.image_surface_copy, self.img_pos)
        
        return self.Surface

    def Toggle_Movement(self):
        self.Moveable = not(self.Moveable)

    def Update_Markers(self, x, y):
        for i in range(len(self.markers_rects)):
            self.markers_rects[i] = pygame.Rect((self.markers_rects[i][0] + x, self.markers_rects[i][1] + y, self.markers_rects[i][2], self.markers_rects[i][3]))
            #self.Elements[Element].position = self.Window_Pos
            #if not(type(Element) == text_class.Text):
            #    self.Elements[Element].rect = pygame.Rect((self.Elements[Element].X_Y_W_H[0] + self.Window_Pos[0], self.Elements[Element].X_Y_W_H[1] + self.Window_Pos[1], self.Elements[Element].X_Y_W_H[2], self.Elements[Element].X_Y_W_H[3]))

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
