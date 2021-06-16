# Імпортуємо необхідні файли та бібліотеки
from kc import *
from kc import Pseudo_Window
from FileManager import *
from win32api import GetMonitorInfo, MonitorFromPoint

# Задаємо необхідні для роботи змінні
Grey_Color = [230, 230, 230]
Salmon_Color = [250, 128, 114]
LightGreen_Color = [144, 238, 144]
White_Color = [255, 255, 255]
Black_Color = [0, 0, 0]
DarkRed_Color = [139, 0, 0]
Enabled_Color = [150, 0, 0]
FPS = 60

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")
print("The work area size is {}x{}.".format(work_area[2], work_area[3]))
Window.width = work_area[2]
Window.height = work_area[3]
Window.Body_Color = Grey_Color
Window.fullscreen = False

# Запускаємо графічне вікно
Window.Start()



def Error_Message(Error):
    Error_Window = Pseudo_Window([Window.width / 2 - 150, Window.height / 2 - 40, 300, 50], [400, 80], FPS = FPS, Body_Color = Salmon_Color)
    Error_Window.Add(Text([10, 10, 300, 50], str(Error), Text_Size=23, rwidth= 350))
    Error_Window.Start()

def Choose_Image():
    try:
        Opened_File = File_Manager(window_resolution = [int(Window.width / 3) , Window.height], window_position=[int(Window.width / 3), 10])
        if Opened_File:
            print("Opened File: ", Opened_File)
            Main_Window.Stop()
            Main_Window.ChangeStore(Opened_File)
    except:
        Error_Message("Неможливо відкрити файл / папку")

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

# Створюємо і додаємо елементи на початкове вікно:
def Main_Window_Create():
    Main_Window = Pseudo_Window([0, 0], [Window.width, Window.height], FPS = FPS)
    Main_Window.Add( Text(  [100, 100, 10, 10], 
                            "Itocia") )
    Main_Window.Add( Input_Field(   [100, 200, 200, 50], 
                                    "Kendize", 
                                    Border_Size=3, 
                                    Enabled_Body_Color=LightGreen_Color))
    Main_Window.Add( Button([300, 400, 300, 40], 
                            "Обрати зображення"), 
                            func = Choose_Image)
    return Main_Window

# Створюємо і додаємо елементи на вікно вибору масштабу:
def Choose_Scale_Window_Create():
    Choose_Scale_Window = Pseudo_Window([int(Window.width / 3), int(Window.width / 80)], [int(Window.width / 3), int(Window.height * 0.5)], FPS = FPS, Moveable=True)
    Choose_Scale_Window.Add(Text([10, 10], "Вкажіть масштаб зображення:", rwidth=int(Window.width / 3) - 40))
    Choose_Scale_Window.Add(Input_Field(X_Y_W_H=[10, 100, int(Window.width / 3) - 20, 50], text="0.19", Enabled_Body_Color=LightGreen_Color))
    Choose_Scale_Window.Add(Button(X_Y_W_H=[10, 200, int(Window.width / 3)-20, 50], text="Наступний крок"), func = Change_Scale_Value)
    return Choose_Scale_Window

# Створюємо і додаємо елементи на вікно роботи з зображенням:
def Image_Showing_Window_Create():
    Image_Showing_Window = Pseudo_Window([0, 0], [Window.width, Window.height], FPS = FPS)
    Image_Showing_Window.Add(Image_Manipulator([5, 5, int(Window.width * 0.85), int(Window.height * 0.9)], Main_Window.Store, Choose_Scale_Window.Store))
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 550, 100, 30], "Delete all markers"), func = Image_Showing_Window.Elements[0].DeleteAllMarkers)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 650, 100, 30], "Create Mask"), func = Image_Showing_Window.Elements[0].Create_Mask)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 750, 100, 30], "Toggle"), func = Image_Showing_Window.Elements[0].Toggle_Mask)
    Image_Showing_Window.Add(Button([int(Window.width * 0.92), 750, 100, 30], "Square"), func = Reload_Square)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 800, 100, 30], "+"), func = Reload_Scale1)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 850, 100, 30], "-"), func = Reload_Scale2)
    Image_Showing_Window.Add(Text([10, int(Window.height * 0.90)], text = "Машстаб: " + str(Image_Showing_Window.Elements[0].Current_Scale)+ " м/піксель"))
    Image_Showing_Window.Add(Text([10, int(Window.height * 0.95)], text = "Площа: " + str(Image_Showing_Window.Elements[0].Calculate_Square())))
    return Image_Showing_Window

while 1:
    Main_Window = Main_Window_Create()
    Main_Window.Start(True)
    if Main_Window.Store == "Closed":
        break
    
    Choose_Scale_Window = Choose_Scale_Window_Create()
    Choose_Scale_Window.Start()
    if Choose_Scale_Window.Store == "Closed":
        continue

    Image_Showing_Window = Image_Showing_Window_Create()
    Image_Showing_Window.Start(True)
    #break
