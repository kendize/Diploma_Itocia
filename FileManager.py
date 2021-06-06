from kc.Pseudo import Pseudo_Window
from kc import *
from file_manager import *
def File_Manager(FPS = 60, 
                Enabled_Body_Color = [255, 130, 130], 
                Enabled_Border_Color = [130, 0, 0], 
                Enabled_Text_Color = [0, 0, 0], 
                Disabled_Body_Color = [230, 230, 230], 
                Disabled_Border_Color = [0, 0, 0], 
                Disabled_Text_Color = [50, 50, 50], 
                Border_Size = 1,
                Path = "Drives"):
    if Path == "Drives":
        Elements = Get_List_Of_Drives()
    else:
        Elements = Get_List_Of_Elements(Path)
    File_Manager_Window = Pseudo_Window([10, 10], [550, 750])

    File_Manager_Loop = True
    while File_Manager_Loop:
        

        Elements = Create_Visual_Elements(
            Elements,
            Disabled_Text_Color = Disabled_Text_Color, 
            Disabled_Body_Color = Disabled_Body_Color, 
            Disabled_Border_Color = Disabled_Border_Color, 
            Border_Size = Border_Size, 
            Enabled_Text_Color = Enabled_Text_Color, 
            Enabled_Body_Color = Enabled_Body_Color, 
            Enabled_Border_Color = Enabled_Border_Color,
            Path = Path
            )

        for Element in Elements:
            File_Manager_Window.Add(Element, Element.text, File_Manager_Window.ChangeStore, File_Manager_Window.Stop, Path, func = Move_To_Path )

        print("Store: ", File_Manager_Window.Store)

        if not(File_Manager_Window.Start()):                                            # Якщо вікно закрите вручну
            return False

        print("NewStore: ", File_Manager_Window.Store)
        if File_Manager_Window.Store == []:
            File_Manager_Window.Store = "Drives"
        if File_Manager_Window.Store == "File":
            return False
        return File_Manager(Path = File_Manager_Window.Store)