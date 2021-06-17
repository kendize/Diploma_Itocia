# Імпортуємо необхідні файли та бібліотеки
from kc import *
from kc import Pseudo_Window
from FileManager import *
from win32api import GetMonitorInfo, MonitorFromPoint
from PIL import Image
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

# Створюємо і додаємо елементи на вікно інформації про программу:
def Author_Window_Create():
    Author_Window = Pseudo_Window([300, 300], [Window.width / 2, Window.height / 3], FPS = FPS, Moveable=True)
    Author_Window.Add( Text(  [10, 10, 10, 10], 
                            "Дипломна робота",
                            Text_Size=40) )
    Author_Window.Add( Text(  [10, 100, 10, 10], 
                            "Тема:",
                            Text_Size=20) )
    Author_Window.Add( Text(  [30, 150, 10, 10], 
                            "Інформаційна технологія аналізу картографічних зображень",
                            Text_Size=20) )
    Author_Window.Add( Text(  [30, 200, 10, 10], 
                            " в системі моніторингу стану ґрунтів Рівненщини",
                            Text_Size=20) )
                            
    Author_Window.Add( Text(  [10, 250, 10, 10], 
                            "Виконав: Окерешко Юрій",
                            Text_Size=25) )
    Author_Window.Add( Text(  [10, 300, 10, 10], 
                            "студент групи КІ-41",
                            Text_Size=25) )                       
    return Author_Window

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
    Main_Window.Add( Button([300, 600, 300, 40], 
                            "Додаткова інформація"), 
                            func = Author_Window.Start)
    return Main_Window

# Створюємо і додаємо елементи на вікно вибору масштабу:
def Choose_Scale_Window_Create():
    Choose_Scale_Window = Pseudo_Window([int(Window.width / 3), int(Window.width / 80)], [int(Window.width / 3), int(Window.height * 0.5)], FPS = FPS, Moveable=True)
    Choose_Scale_Window.Add(Text([10, 10], "Вкажіть масштаб зображення:", rwidth=int(Window.width / 3) - 40))
    Choose_Scale_Window.Add(Input_Field(X_Y_W_H=[10, 100, int(Window.width / 3) - 20, 50], text="0.19", Enabled_Body_Color=LightGreen_Color))
    Choose_Scale_Window.Add(Button(X_Y_W_H=[10, 200, int(Window.width / 3)-20, 50], text="Наступний крок"), func = Change_Scale_Value)
    return Choose_Scale_Window

# Створюємо і додаємо елементи на вікно інформації про зображення:
def Image_Information_Window_Create():
    Path = Main_Window.Store
    Image_Information_Window = Pseudo_Window([int(Window.width / 3), int(Window.width / 80)], [int(Window.width / 3), int(Window.height * 0.5)], FPS = FPS, Moveable=True)
    image = pygame.image.load(Path)
    ImageObj = Image.open(Path)
    
    Image_Information_Window.Add( Text(  [20, 20, 10, 10], 
                                "Роздільна здатність: " + str(image.get_width())+" x "+str(image.get_height())) )
    size = float(os.stat(Path).st_size / 1024)
    if size > 1024:
        size = str( round(float(size / 1024), 2)) + " Мб"
    else:
        size = str( round(size, 2)) + " Кб"

    Image_Information_Window.Add( Text(  [20, 70, 10, 10], 
                                "Розмір файлу: " + size) )
    Image_Information_Window.Add( Text(  [20, 120, 10, 10], 
                                "Шлях до файлу: " + ImageObj.filename) )                           
    Image_Information_Window.Add( Text(  [20, 170, 10, 10], 
                                "Формат файлу: " + ImageObj.format) )
    ImageObj = ImageObj.mode
    if ImageObj == "1":
        ImageObj = "1 біт, чорний або білий"
    elif ImageObj == "L":
        ImageObj = "8 біт, відтінки сірого"
    elif ImageObj == "P":
        ImageObj = "8 біт, 256 кольорів"
    elif ImageObj == "RGB":
        ImageObj = "3x8 біт, True Color"
    elif ImageObj == "RGBA":
        ImageObj = "4x8 біт, True Color з прозорістю"
    else:
        ImageObj == "Невідомо"
    Image_Information_Window.Add( Text(  [20, 220, 10, 10], 
                                "Тип і Глибина кольору: " + ImageObj) )                     
    #print("Размер файла:", os.stat(Path).st_rsize)
    return Image_Information_Window

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
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 450, 100, 30], "Інформація"), func = Image_Information_Window.Start)
    Image_Showing_Window.Add(Button([int(Window.width * 0.87), 350, 100, 30], "Кольори"), func = Top_Colors_Helper)
    return Image_Showing_Window

def Top_Colors_Window_Create(Colors):
    Top_Colors_Window = Pseudo_Window([int(Window.width / 6), int(Window.height / 80)], [int(2 * Window.width / 3), int(Window.height * 0.9)], FPS = FPS, Moveable=True)
    number_of_colors = len(Colors[0])
    row = 0
    data = 0
    for i in range(number_of_colors):
        Top_Colors_Window.Add(Button(
            [10 + row * int(Window.width / 8), int(Window.height / 20 + data * int(Window.width / 30)), int(Window.width / 9), int(Window.height / 20)], 
            text = str(Colors[0][i]) + " : " + str(Colors[1][i]),
            Disabled_Body_Color=([int(i) for i in Colors[0][i][1:-1].split(", ")]),
            Disabled_Text_Color=[255, 255, 255]
        ))
        row += 1
        if row > 4:
            data += 1
            row = 0
    return Top_Colors_Window

def Top_Colors_Helper():
    try:
        Colors = Image_Showing_Window.Elements[0].Top_Colors()
        Top_Colors_Window = Top_Colors_Window_Create(Colors)
        Top_Colors_Window.Start()
    except:
        return

while 1:
    Author_Window = Author_Window_Create()
    Main_Window = Main_Window_Create()
    
    Main_Window.Start(True)
    if Main_Window.Store == "Closed":
        break
    Image_Information_Window = Image_Information_Window_Create()
    Choose_Scale_Window = Choose_Scale_Window_Create()
    Choose_Scale_Window.Start()
    if Choose_Scale_Window.Store == "Closed":
        continue

    Image_Showing_Window = Image_Showing_Window_Create()
    Image_Showing_Window.Start(True)
    if Image_Showing_Window.Store == "Closed":
        continue
    #break
