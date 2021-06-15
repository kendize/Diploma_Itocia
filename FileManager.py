from kc.invis_scroll import Invis_Scroll
from kc.Pseudo import Pseudo_Window
from kc import *
from file_manager import *

def File_Manager(FPS = 60, 
                Enabled_Body_Color = [144, 238, 144], 
                Enabled_Border_Color = [130, 0, 0], 
                Enabled_Text_Color = [0, 0, 0], 
                Disabled_Body_Color = [230, 230, 230], 
                Disabled_Border_Color = [0, 0, 0], 
                Disabled_Text_Color = [50, 50, 50], 
                Border_Size = 1,
                Path = "Drives",
                window_resolution = [550, 750],
                window_position = [10, 10]
                ):
    #window_resolution = [550, 750]
    #window_position = [10, 10]

    def Scroll():
        if File_Manager_Window.Elements[1].X_Y_W_H[1] < 0 or File_Manager_Window.Elements[-2].X_Y_W_H[1] > (window_resolution[1]-50):
            for i in range(len(File_Manager_Window.Elements) - 2):
                File_Manager_Window.Elements[i + 1].X_Y_W_H[1] += File_Manager_Window.Elements[0].y
            File_Manager_Window.Update_Elements()
    if Path == "Drives":
        Elements = Get_List_Of_Drives()
    else:
        Elements = Get_List_Of_Elements(Path)

    File_Manager_Window = Pseudo_Window(window_position, window_resolution)
    File_Manager_Loop = True
    while File_Manager_Loop:
        File_Manager_Window.Add(Invis_Scroll(0), func = Scroll)
        Elements = Create_Visual_Elements(
            File_Manager_Window.Elements[0].y,
            Elements,
            Disabled_Text_Color = Disabled_Text_Color, 
            Disabled_Body_Color = Disabled_Body_Color, 
            Disabled_Border_Color = Disabled_Border_Color, 
            Border_Size = Border_Size, 
            Enabled_Text_Color = Enabled_Text_Color, 
            Enabled_Body_Color = Enabled_Body_Color, 
            Enabled_Border_Color = Enabled_Border_Color,
            Path = Path,
            width=int(window_resolution[0] * 0.95)
            )
        
        #print(File_Manager_Window.Elements[1])

        for Element in Elements:
            File_Manager_Window.Add(Element, Element.text, File_Manager_Window.ChangeStore, File_Manager_Window.Stop, Path, func = Move_To_Path )
        
        print("Store: ", File_Manager_Window.Store)

        File_Manager_Window.Start()                                           # Якщо вікно закрите вручну
        
        print("NewStore: ", File_Manager_Window.Store)
        if File_Manager_Window.Store == []:
            File_Manager_Window.Store = "Drives"
        if File_Manager_Window.Store[0] == "!":
            return File_Manager_Window.Store[1:]
        if File_Manager_Window.Store == "Closed":
            return
        return File_Manager(Path = File_Manager_Window.Store, window_resolution = window_resolution,
                window_position = window_position)