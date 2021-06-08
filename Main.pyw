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
    try:
        Opened_File = File_Manager()
        if Opened_File:
            Main_Window.Stop()
            Main_Window.ChangeStore(Opened_File)
            #Main_Window.Add(Text([100, 500, 100, 100], Main_Window.Store))
            #Main_Window.Add(Image([500, 500], Opened_File))
    except:
        Error_Window = Pseudo_Window([300, 850], [400, 50], FPS = FPS, Body_Color=[250, 128, 114])
        Error_Window.Add(Text([0, 0, 200, 50], "Error in import file", Text_Size=23))
        Error_Window.Start()


Main_Window = Pseudo_Window([0, 0], [1200, 900], FPS = FPS)
Main_Window.Add( Text([100, 100, 100, 100], "Hello") )
Main_Window.Add( Input_Field([100, 200, 200, 50], "Kendize", Border_Size=3))
Main_Window.Add( Button([300, 400, 100, 30], "Test window"), func = Choose_Image)

Main_Window.Start(True)

Image_Showing_Window = Pseudo_Window([0, 0], [1200, 900], FPS = FPS)

Image_Showing_Window.Add(Image([0, 100], Main_Window.Store, Moveable=True))
Image_Showing_Window.Add(Button([300, 400, 100, 30], "Test window"))
Image_Showing_Window.Start(True)

