# kc -( kendize classes )- my own library for my projects.
from kc import *
from kc import Pseudo_Window
from FileManager import *
# Here I am creating some variables for initialization of window for my purposes
from win32api import GetMonitorInfo, MonitorFromPoint

Grey_Color = [230, 230, 230]
Salmon_Color = [250, 128, 114]
LightGreen_Color = [144, 238, 144]
White_Color = [255, 255, 255]
Black_Color = [0, 0, 0]
DarkRed_Color = [139, 0, 0]

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")
print("The work area size is {}x{}.".format(work_area[2], work_area[3]))
Window.width = work_area[2]
Window.height = work_area[3]
Window.Body_Color = Grey_Color
Window.fullscreen = False
Window.Start()

Enabled_Color = [150, 0, 0]
FPS = 60

def Error_Message(Error):
    Error_Window = Pseudo_Window([300, 850], [400, 50], FPS = FPS, Body_Color = Salmon_Color)
    Error_Window.Add(Text([10, 10, 200, 50], str(Error), Text_Size=23))
    Error_Window.Start()

def Choose_Image():
    try:
        Opened_File = File_Manager(window_resolution = [Window.width, Window.height], window_position=[0, 0])
        if Opened_File:
            print("Opened File: ", Opened_File)
            Main_Window.Stop()
            Main_Window.ChangeStore(Opened_File)
            #Main_Window.Add(Text([100, 500, 100, 100], Main_Window.Store))
            #Main_Window.Add(Image([500, 500], Opened_File))
    except:
        Error_Message("Cannot open folder/file")

def Change_Scale_Value():
    try:
        Choose_Scale_Window.ChangeStore(float(Choose_Scale_Window.Elements[1].text))
        Choose_Scale_Window.Stop()
    except:
        Error_Message("Неправильний масштаб!")
    
def Reload_Square():
    Image_Showing_Window.Elements[8].Render("Площа: " + str(Image_Showing_Window.Elements[0].Calculate_Square()))

def Reload_Scale1():
    Image_Showing_Window.Elements[0].ZoomIn()
    Image_Showing_Window.Elements[7].Render("Машстаб: " + str(Image_Showing_Window.Elements[0].Current_Scale) + " м/піксель")
    

def Reload_Scale2():
    Image_Showing_Window.Elements[0].ZoomOut()
    Image_Showing_Window.Elements[7].Render("Машстаб: " + str(Image_Showing_Window.Elements[0].Current_Scale) + " м/піксель")
    
while 1:
    Main_Window = Pseudo_Window([0, 0], [Window.width, Window.height], FPS = FPS)
    Main_Window.Add( Text([100, 100, 10, 10], "Itocia") )
    Main_Window.Add( Input_Field([100, 200, 200, 50], "Kendize", Border_Size=3, Enabled_Body_Color=LightGreen_Color))
    Main_Window.Add( Button([300, 400, 300, 40], "Обрати зображення"), func = Choose_Image)

    Main_Window.Start(True)

    if Main_Window.Store == "Closed":
        break

    #Main_Window.ChangeStore("e:\Pictures\\223.jpg")
    Choose_Scale_Window = Pseudo_Window([int(Window.width / 3), int(Window.width / 80)], [int(Window.width / 3), int(Window.height * 0.9)], FPS = FPS)
    Choose_Scale_Window.Add(Text([10, 10], "Вкажіть масштаб зображення:"))
    Choose_Scale_Window.Add(Input_Field(X_Y_W_H=[10, 100, int(Window.width / 4), 50], text="0.19"))
    Choose_Scale_Window.Add(Button(X_Y_W_H=[10, 200, int(Window.width / 4), 50], text="Наступний крок"), func = Change_Scale_Value)
    Choose_Scale_Window.Start()


    Image_Showing_Window = Pseudo_Window([0, 0], [Window.width, Window.height], FPS = FPS)

    Image_Showing_Window.Add(Image([5, 5, int(Window.width * 0.85), int(Window.height * 0.9)], Main_Window.Store, Choose_Scale_Window.Store, Moveable=True))
    
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 550, 100, 30], "Delete all markers"), func = Image_Showing_Window.Elements[0].DeleteAllMarkers)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 650, 100, 30], "Create Mask"), func = Image_Showing_Window.Elements[0].Create_Mask)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 750, 100, 30], "Toggle"), func = Image_Showing_Window.Elements[0].Toggle_Mask)
    Image_Showing_Window.Add(Button([int(Window.width * 0.92), 750, 100, 30], "Square"), func = Reload_Square)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 800, 100, 30], "+"), func = Reload_Scale1)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 850, 100, 30], "-"), func = Reload_Scale2)

    Image_Showing_Window.Add(Text([0, 0], text = "Машстаб: " + str(Image_Showing_Window.Elements[0].Current_Scale)+ " м/піксель"))
    Image_Showing_Window.Add(Text([0, 100], text = "Площа: " + str(Image_Showing_Window.Elements[0].Calculate_Square())))
    Image_Showing_Window.Start(True)
    #break
