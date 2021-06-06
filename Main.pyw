# kc -( kendize classes )- my own library for my projects. First steps)
from kc import *
from kc import Pseudo_Window
from FileManager import *
# Here I am creating some variables for initialization of window for my purposes

Window.width = 1200
Window.height = 900
Window.Body_Color = [230, 230, 230]
Window.fullscreen = False
Window.Start()

Enabled_Color = [150, 0, 0]
FPS = 60

def Choose_Image():
    File_Manager()
    return
Main_Window = Pseudo_Window([0, 0], [1200, 900], FPS = FPS)
Test_Window = Pseudo_Window([100, 100], [200, 200], Moveable=True, FPS=FPS)
Main_Window.Add( Text([100, 100, 100, 100], "Hello") )
Main_Window.Add( Input_Field([100, 200, 200, 50], "Kendize"))
Main_Window.Add( Button([300, 400, 100, 30], "Test window"), func = Choose_Image)
#Main_Window.Add( Button([300, 500, 100, 30], "Delete Elements"), func = Main_Window.RemoveAllElements)

Main_Window.Start(True)


    
