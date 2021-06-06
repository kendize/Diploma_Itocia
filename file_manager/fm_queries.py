from win32api import GetLogicalDriveStrings
import os

def Get_List_Of_Drives():                                                              # Функція для знаходження логічних дисків
    drives = GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    for i in range(len(drives)):
        drives[i] = os.path.normcase(drives[i])
    return drives 

def Get_List_Of_Elements(Current_Path):                                                            # Функція для знаходження всіх елементів
    Output = os.listdir(os.path.normpath(Current_Path))
    #Output = os.listdir(os.getcwd())
    List_Of_Folders = []
    List_Of_Files = []

    for Element in Output:
        if os.path.isfile(os.path.join(Current_Path, Element)):
            List_Of_Files.append(Element)
        if os.path.isdir(os.path.join(Current_Path, Element)):
            List_Of_Folders.append(Element)

    List_Of_Elements = [List_Of_Folders, List_Of_Files]
    return List_Of_Elements

def isDrives(Path):
    if Path in Get_List_Of_Drives():
        return True
    return False