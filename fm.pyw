from library.kendize_engine import *
from win32api import GetLogicalDriveStrings
import os

def Find_Drives():                                                              # Функція для знаходження логічних дисків
    drives = GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    for i in range(len(drives)):
        drives[i] = os.path.normcase(drives[i])
    return drives 

def Elements_List():                                                            # Функція для знаходження всіх елементів
    Output = os.listdir(os.getcwd())
    List_Of_Folders = []
    List_Of_Files = []

    for Element in Output:
        if os.path.isfile(Element):
            List_Of_Files.append(Element)
        if os.path.isdir(Element):
            List_Of_Folders.append(Element)


    
    List_Of_Elements = [List_Of_Folders, List_Of_Files]
    return List_Of_Elements

def Change_Directory(Path):                                                     # Функція для зміни директорії
    try:
        
        if Path == "..":
           
            Path = os.path.abspath(os.path.join(str(os.getcwd()), '..'))
            os.chdir(Path)
            
        else:
            Path = os.path.abspath(os.path.join(str(os.getcwd()), Path))
            os.chdir(Path)

        return True

    except:
        return False

def Create_Visual_Elements(Disabled_Text_Color, Disabled_Body_Color, Disabled_Border_Color, Border_Size, Enabled_Text_Color, Enabled_Body_Color, Enabled_Border_Color, Switch = True, variable = False):                                                   # Функція для створення візуальної презентації елементів
    
    x = 10
    y = 10
    w = 500
    h = 35

    text_size = 17
    Elements = []
    if not(variable):
        delme = Elements_List()
        obj = delme[0]
        obj.extend(delme[1])
        Elements.append(Button(
                [x, y, w, h], "..", text_size, Disabled_Text_Color, Disabled_Body_Color, Disabled_Border_Color, Border_Size, Enabled_Text_Color, Enabled_Body_Color, Enabled_Border_Color, Switch = True
            ))
    else:
        obj = Find_Drives()
    for Number in range(len(obj)):
        Elements.append(Button(
            [x, y+(h - 1)*(Number + 1), w, h], obj[Number], text_size, Disabled_Text_Color, Disabled_Body_Color, Disabled_Border_Color, Border_Size, Enabled_Text_Color, Enabled_Body_Color, Enabled_Border_Color, Switch = True
        ))
    for Number in range(len(Elements)):
        Elements[Number].Switch = True
    return Elements

def Draw_Everything(*obj):                                                      # Функція для виведення всіх об'єктів
    Window.surface.fill(Window.Body_Color)
    for a in obj:
        for b in range(len(a)):
            a[b].Draw()

def Drives_Place(Path):
    if Path in Find_Drives():
        return True
    return False

def File_Manager(Main_Loop, Drives, Elements, FPS, Enabled_Body_Color, Enabled_Border_Color, Enabled_Text_Color, Disabled_Body_Color, Disabled_Border_Color, Disabled_Text_Color, Border_Size):
    while Main_Loop:                                                            # Запускаємо головний цикл
        for Event in event.get():                                               # Перевірка подій
            if Event.type == QUIT:                                              # Вихід з програми
                Main_Loop = False
            for i in range(len(Elements)):
                if Elements[i].Check(Event):
                    if not(Elements[i].Active):
                        if os.path.abspath(os.getcwd()) in Find_Drives() and Elements[i].text == "..":

                            Elements = Create_Visual_Elements(Disabled_Text_Color, 
                                Disabled_Body_Color, 
                                Disabled_Border_Color, 
                                Border_Size, 
                                Enabled_Text_Color, 
                                Enabled_Body_Color, 
                                Enabled_Border_Color, 
                                Switch = True, 
                                variable = True)

                            Draw_Everything(Elements)
                            break

                        else:  
                            Window.surface.fill(Window.Body_Color)
                            Change_Directory(Elements[i].text)
                            

                            Elements = Create_Visual_Elements(Disabled_Text_Color, 
                                Disabled_Body_Color, 
                                Disabled_Border_Color, 
                                Border_Size, 
                                Enabled_Text_Color, 
                                Enabled_Body_Color, 
                                Enabled_Border_Color, 
                                Switch = True, 
                                variable = False)

                            Draw_Everything(Elements)

                            print("Current path: ", os.path.abspath(os.getcwd()))
                            
                            break
        Update(FPS)

def __main__():
    global Main_Loop, Drives, Elements
    Main_Loop = True                                                            # Змінна циклу
    Drives = Find_Drives()                                                      # Знаходимо логічні диски
    Elements = Drives                                                           # Початковий список елементів - список логічних дисків
    
    # Змінні для побудови вікна
    FPS = 60
    Window.width = 800
    Window.height = 600
    Window.Body_Color = [255, 255, 255]
    Window.Start()
    # Змінні кольорової схеми програми
    Enabled_Body_Color = [255, 130, 130]
    Enabled_Border_Color = [130, 0, 0]
    Enabled_Text_Color = [0, 0, 0]

    Disabled_Body_Color = [230, 230, 230]
    Disabled_Border_Color = [0, 0, 0]
    Disabled_Text_Color = [50, 50, 50]

    Border_Size = 1
    Elements = Create_Visual_Elements(Disabled_Text_Color, 
        Disabled_Body_Color, 
        Disabled_Border_Color, 
        Border_Size, 
        Enabled_Text_Color, 
        Enabled_Body_Color, 
        Enabled_Border_Color, 
        Switch = True, 
        variable = True)

    Draw_Everything(Elements)
    
    File_Manager(Main_Loop, 
        Drives, 
        Elements, 
        FPS, 
        Enabled_Body_Color, 
        Enabled_Border_Color, 
        Enabled_Text_Color, 
        Disabled_Body_Color, 
        Disabled_Border_Color, 
        Disabled_Text_Color, 
        Border_Size)
        

if __name__ == "__main__":
    __main__()