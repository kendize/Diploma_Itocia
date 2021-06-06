#from file_manager.fm_queries import Get_List_Of_Drives, isDrives
from fm import File_Manager
from file_manager.fm_queries import *
from kc import *
import os
def Move_To_Path(obj, Store, Stop, Path):                                                     # Функція для зміни директорії
    global Current_Path
    try:
        if (Path in Get_List_Of_Drives()) and (obj == ".."):                                  # Перехід до директорії з дисками
            Store("Drives")
            Stop()
            return
        Current_Path = os.path.abspath(os.path.join(str(Path), obj))
        if os.path.isfile(Current_Path):
            Store("File")
            Stop()
            return
        Store(Current_Path)
        Stop()
        return Current_Path, Store

    except:
        return False

def Create_Visual_Elements(*args, Disabled_Text_Color, Disabled_Body_Color, Disabled_Border_Color, Border_Size, Enabled_Text_Color, Enabled_Body_Color, Enabled_Border_Color, isDrives = False, Path):                                                   # Функція для створення візуальної презентації елементів
    
    x = 3
    y = 3
    w = 500
    h = 35
    text_size = 17
    Elements = []
    if not(isDrives) and not(Path == "Drives"):
        tempObj = Get_List_Of_Elements(Path)
        obj = [".."]
        obj.extend(tempObj[0])
        obj.extend(tempObj[1])
    else:
        obj = Get_List_Of_Drives()
    for Number in range(len(obj)):
        Elements.append(Button(
            X_Y_W_H = [x, y+(h - 1)*(Number + 1), w, h],
            text = obj[Number], 
            Text_Size = text_size, 
            Disabled_Text_Color = Disabled_Text_Color, 
            Disabled_Body_Color = Disabled_Body_Color, 
            Disabled_Border_Color = Disabled_Border_Color, 
            Border_Size = Border_Size, 
            Enabled_Text_Color = Enabled_Text_Color, 
            Enabled_Body_Color = Enabled_Body_Color, 
            Enabled_Border_Color = Enabled_Border_Color, 
            Switch = True
        ))

    return Elements

def Draw_Elements(*obj):                                                      # Функція для виведення всіх об'єктів
    #Window.surface.fill(Window.Body_Color)
    for a in obj:
        for b in range(len(a)):
            a[b].Draw()