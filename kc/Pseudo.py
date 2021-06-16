from kc import text_class
from kc import *
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

class Pseudo_Window(object):
    def __init__(self, Window_Pos, Window_Res, Moveable = False, Body_Color = [230, 230, 230], Border_Size = 2, Border_Color = [0, 0, 0], FPS = 60, BackGround = False):
        self.Window_Pos = Window_Pos
        self.Window_Res = Window_Res
        self.Body_Color = Body_Color
        self.Border_Size = Border_Size
        self.Border_Color = Border_Color
        self.Elements = []#[Button([Window_Res[0] - 38, 2, 40, 30], "/img/close.png", position = self.Window_Pos, Border_Size= 0, Disabled_Body_Color = [230, 230, 230])]
        self.functions = []#[self.Stop]#[False]
        self.arguments = []#[False]
        self.surface = pygame.Surface(self.Window_Res)
        self.Moveable = Moveable
        self.Move = False
        self.FPS = FPS
        self.Loop = True
        self.Store = []
        self.BackGround = BackGround

    def AddCloseButton(self):
        self.Add(Button([self.Window_Res[0] - 38, 2, 40, 30], "/img/close.png", position = self.Window_Pos, Border_Size= 0, Disabled_Body_Color = [230, 230, 230]), func=self.Close)

    def ChangeStore(self, info):
        print("Pseudo: Changing Store :", info)
        self.Store = info


    def Add(self, Element, *args, func = False):
        if not(type(Element) == text_class.Text):
            Element.position = self.Window_Pos
            Element.rect = pygame.Rect((Element.X_Y_W_H[0] + Element.position[0], Element.X_Y_W_H[1] + Element.position[1],Element.X_Y_W_H[2], Element.X_Y_W_H[3]))
        self.Elements.append(Element)
        self.functions.append(func)
        self.arguments.append([args])
    
    def Stop(self):
        self.Loop = False
        #self.ChangeStore("Closed")
        print("Pseudo Stopped")
    
    def Close(self):
        self.Loop = False
        self.ChangeStore("Closed")
        print("Pseudo Stopped")

    def Update_Elements(self):
        for Element in range(len(self.Elements)):
            self.Elements[Element].position = self.Window_Pos
            if not(type( self.Elements[Element]) == text_class.Text):
                self.Elements[Element].rect = pygame.Rect((self.Elements[Element].X_Y_W_H[0] + self.Window_Pos[0], self.Elements[Element].X_Y_W_H[1] + self.Window_Pos[1], self.Elements[Element].X_Y_W_H[2], self.Elements[Element].X_Y_W_H[3]))

    def Draw(self, update = True):
        self.surface.fill(self.Body_Color)
        pygame.draw.rect(self.surface, self.Border_Color, [0, 0, self.Window_Res[0] - (self.Border_Size - 1), self.Window_Res[1] - (self.Border_Size - 1)], self.Border_Size)
        for Element in self.Elements:
            Draw(Element, self.surface)
        Window.surface.blit(self.surface, (self.Window_Pos[0], self.Window_Pos[1]))
        if update:
            Update(self.FPS)

    def Start(self, Looped = False):
        self.AddCloseButton()
        if self.BackGround:
            copy = self.BackGround
            self.BackGround = copy
            #copy1 = self.BackGround.copy().convert_alpha()
        else:
            copy = Window.surface.copy()
            copy1 = Window.surface.copy().convert_alpha()
            copy1.fill((0, 0, 0, 100))
            copy.blit(copy1, [0, 0, copy.get_width(), copy.get_height()], None, 0)
            copy = copy.convert(copy)
        
        #copy.blit(copy, [0, 0, copy.get_width(), copy.get_height()], None, pygame.BLEND_RGBA_MULT)
        #copy.blit(copy, [0, 0, copy.get_width(), copy.get_height()], None, pygame.BLEND_RGBA_MULT)
        Not_Active = [
            Text,
            Box
        ]
        #Loop = True
        while self.Loop:
            for Event in pygame.event.get():
                #if self.Elements[0].Check(Event):
                #    self.Stop()
                #    return False

                for Element in range(len(self.Elements)):
                    if not(type(self.Elements[Element]) in Not_Active):
                        if self.Elements[Element].Check(Event) and self.functions[Element]:
                            Draw(self.Elements[Element], self.surface)
                            Window.surface.blit(self.surface, (self.Window_Pos[0], self.Window_Pos[1]))
                            pygame.display.update()
                            if (not( self.arguments[Element] == [()] )):
                                if len(self.arguments[Element][0]) == 1:
                                    
                                    if self.functions[Element](self.arguments[Element][0]) == True:
                                        #Loop = False
                                        if Looped:
                                            return self.Start(True)
                                        return True
                                if len(self.arguments[Element][0]) == 2:
                                    if self.functions[Element](self.arguments[Element][0][0], self.arguments[Element][0][1]) == True:
                                        #Loop = False
                                        if Looped:
                                            return self.Start(True)
                                        return True
                                if len(self.arguments[Element][0]) == 3:
                                    if self.functions[Element](self.arguments[Element][0][0], self.arguments[Element][0][1], self.arguments[Element][0][2]) == True:
                                        #Loop = False
                                        if Looped:
                                            return self.Start(True)
                                        return True
                                if len(self.arguments[Element][0]) == 4:
                                    if self.functions[Element](self.arguments[Element][0][0], self.arguments[Element][0][1], self.arguments[Element][0][2], self.arguments[Element][0][3]) == True:
                                        #Loop = False
                                        if Looped:
                                            return self.Start(True)
                                        return True
                            else:
                                if self.functions[Element]() == True:
                                    #Loop = False
                                    if Looped:
                                        return self.Start(True)
                                    return True

                
                if self.Moveable:
                    if Event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.Rect(self.Window_Pos, self.Window_Res).collidepoint(Event.pos):
                            if Event.button == 3:
                                self.Move = True
                    if Event.type == pygame.MOUSEBUTTONUP:
                        if Event.button == 3:
                            self.Move = False
                    if self.Move:
                        if Event.type == pygame.MOUSEMOTION:
                            self.Window_Pos[0] += Event.rel[0]
                            self.Window_Pos[1] += Event.rel[1]
                            self.Update_Elements()
            
            Window.surface.blit(copy, (0, 0))

            self.Draw()
        return True