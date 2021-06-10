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

def Error_Message(Error):
    Error_Window = Pseudo_Window([300, 850], [400, 50], FPS = FPS, Body_Color=[250, 128, 114])
    Error_Window.Add(Text([10, 10, 200, 50], str(Error), Text_Size=23))
    Error_Window.Start()

def Choose_Image():
    try:
        Opened_File = File_Manager()
        if Opened_File:
            print("Opened File: ", Opened_File)
            Main_Window.Stop()
            Main_Window.ChangeStore(Opened_File)
            #Main_Window.Add(Text([100, 500, 100, 100], Main_Window.Store))
            #Main_Window.Add(Image([500, 500], Opened_File))
    except:
        Error_Message("Cannot open folder/file")


while 1:
    Main_Window = Pseudo_Window([0, 0], [Window.width, Window.height], FPS = FPS)
    Main_Window.Add( Text([100, 100, 10, 10], "Itocia") )
    Main_Window.Add( Input_Field([100, 200, 200, 50], "Kendize", Border_Size=3, Enabled_Body_Color=[144, 238, 144]))
    Main_Window.Add( Button([300, 400, 100, 30], "Test window"), func = Choose_Image)
#
#
    Main_Window.Start(True)
    if Main_Window.Store == "Closed":
        break
    #Main_Window.ChangeStore("e:\Pictures\\222.jpg")
    Image_Showing_Window = Pseudo_Window([0, 0], [Window.width, Window.height], FPS = FPS)
    Image_Showing_Window.Add(Image([0, 0, 900, 700], Main_Window.Store, 0.19, Moveable=True))
    Image_Showing_Window.Add(Button([920, 550, 100, 30], "Delete all markers"), func = Image_Showing_Window.Elements[0].DeleteAllMarkers)
    Image_Showing_Window.Add(Button([920, 650, 100, 30], "Create Mask"), func = Image_Showing_Window.Elements[0].Create_Mask)
    Image_Showing_Window.Add(Button([920, 750, 100, 30], "Toggle"), func = Image_Showing_Window.Elements[0].Toggle_Mask)

    Image_Showing_Window.Add(Button([920, 800, 100, 30], "+"), func = Image_Showing_Window.Elements[0].ZoomIn)
    Image_Showing_Window.Add(Button([920, 850, 100, 30], "-"), func = Image_Showing_Window.Elements[0].ZoomOut)

    Image_Showing_Window.Start(True)
    break
