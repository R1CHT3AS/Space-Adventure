import ResourceHandler as RH
import PrintHandler as PH
import ColonistHandler as CH
import BuildingsHandler as BH
start = 1
def game():
    PH.PrintHandler().FilePrint("StartScreen.txt")
    Choice = input()
    if Choice == "1":
        quit()
    elif Choice == "2":
        SaveFile = input("Enter the name of the save file: ")
    elif Choice == "3":
        PH.PrintHandler().FilePrint("Start.txt")
        rh = RH.ResourceHandler("MainResourceFile.txt")
        PH.PrintHandler().FilePrint("MainResourceFile.txt")
        ch = CH.ColonistHandler("MainColonistFile.txt")
        PH.PrintHandler().FilePrint("MainColonistFile.txt")
        bh = BH.BuildingsHandler("MainBuildingFile.txt")
        PH.PrintHandler().FilePrint("BuildingsScreen.txt")
if start == 1:
    game()