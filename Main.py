import ResourceHandler as RH
import PrintHandler as PH
import ColonistHandler as CH
import BuildingsHandlerFile as BH

start = 1

def Start():
    PH.PrintHandler().FilePrint("StartScreen.txt", True)
    Choice = input()
    if Choice == "1":
        quit()
    elif Choice == "2":
        SaveFile = input("Enter the name of the save file: ")
    elif Choice == "3":
        PH.PrintHandler().FilePrint("Start.txt", False)
        rh = RH.ResourceHandler("MainResourceFile.txt")
        PH.PrintHandler().FilePrint("MainResourceFile.txt", False)
        ch = CH.ColonistHandler("MainColonistFile.txt")
        PH.PrintHandler().FilePrint("MainColonistFile.txt", False)
        PH.PrintHandler().FilePrint("Help.txt", False)

def Game(Choice):
    if "!" in Choice:
        if Choice == "!Buildings":
            bh = BH.BuildingsHandlerFile("MainBuildingFile.txt")
            bh.BuildingScreen()
        elif Choice == "!Help":
            PH.PrintHandler().FilePrint("Help.txt", False)
        elif Choice == "!Resources":
            PH.PrintHandler().FilePrint("MainResourceFile.txt", False)
        elif Choice == "!Colonists":
            PH.PrintHandler().FilePrint("MainColonistFile.txt", False)
    else:
        return Choice
    Game(input("What do you want to do?"))
if start == 1:
    start = 0
    Start()
    Game(input("What do you want to do?"))

