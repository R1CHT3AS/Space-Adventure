import os
import PrintHandler as PH


class BuildingsHandlerFile:
    def __init__(self, ID):
        print("BuildingHandler initializing...")
        self.HydroponicsLvl = 2
        self.IHCLvl = 1
        self.ArbouretumLvl = 1
        self.FusionReactorLvl = 1
        self.CrewChambersLvl = 1
        self.AMSLvl = 1
        self.HospitalLvl = 1
        self.SpaLvl = 1

        self.HydroponicsProduction = self.GetProduction("Hydroponics", self.HydroponicsLvl)
        self.IHCProduction = self.GetProduction("IHC", self.IHCLvl)
        self.ArbouretumProduction = self.GetProduction("Arbouretum", self.ArbouretumLvl)
        self.FusionReactorProduction = self.GetProduction("FusionReactor", self.FusionReactorLvl)
        self.CrewChambersProduction = self.GetProduction("CrewChambers", self.CrewChambersLvl)
        self.AMSProduction = self.GetProduction("AMS", self.AMSLvl)
        self.HospitalProduction = self.GetProduction("Hospital", self.HospitalLvl)
        self.SpaProduction = self.GetProduction("Spa", self.SpaLvl)

        if not os.path.exists(ID):
            self.create_text_file(ID)
        self.update_text_file(ID)

    def create_text_file(self, filename):
        with open(filename, 'w') as file:
            file.write("")
        print(f"File '{filename}' created successfully.")

    def update_text_file(self, filename):
        with open(filename, 'w') as file:
            file.write(
                "Hydroponics Level = " + str(self.HydroponicsLvl) + "\n" +
                "Ice Harvesting Center Level = " + str(self.IHCLvl) + "\n" +
                "Arbouretum Level = " + str(self.ArbouretumLvl) + "\n" +
                "Fusion Reactor Level = " + str(self.FusionReactorLvl) + "\n" +
                "Crew Chambers Level = " + str(self.CrewChambersLvl) + "\n" +
                "Atmosphere Management System Level = " + str(self.AMSLvl) + "\n" +
                "Hospital Level = " + str(self.HospitalLvl) + "\n" +
                "Spa Level = " + str(self.SpaLvl)
            )

    def SpecificBuildingScreen(self, choice):
        from Main import Game
        if choice == "1":
            print("Hydroponics Level = " + str(self.HydroponicsLvl))
            print("Hydroponics Production = " + str(self.HydroponicsProduction))
        elif choice == "2":
            print("Interstellar Hydrogen Collectors Level = " + str(self.IHCLvl))
            print("IHC Production = " + str(self.IHCProduction))
        elif choice == "3":
            print("Arbouretum Level = " + str(self.ArbouretumLvl))
            print("Arbouretum Production = " + str(self.ArbouretumProduction))
        elif choice == "4":
            print("Fusion Reactor Level = " + str(self.FusionReactorLvl))
            print("Fusion Reactor Production = " + str(self.FusionReactorProduction))
        elif choice == "5":
            print("Crew Chambers Level = " + str(self.CrewChambersLvl))
            print("Crew Chambers Production = " + str(self.CrewChambersProduction))
        elif choice == "6":
            print("Atmosphere Management System Level = " + str(self.AMSLvl))
            print("AMS Production = " + str(self.AMSProduction))
        elif choice == "7":
            print("Hospital Level = " + str(self.HospitalLvl))
            print("Hospital Production = " + str(self.HospitalProduction))
        elif choice == "8":
            print("Spa Level = " + str(self.SpaLvl))
            print("Spa Production = " + str(self.SpaProduction))
        else:
            print("Invalid choice. Please try again.")
            self.BuildingScreen(input("What do you want to do?"))
        slection = Game(input("What do you want to do?" + "\n" + "1. Upgrade Building" + "\n" + "2. Go back" + "\n"))
        if slection == "1":
            self.UpgradeBuilding(choice)
        elif slection == "2":
            PH.PrintHandler().FilePrint("BuildingsScreen.txt", False)
            self.BuildingScreen()

    def GetProduction(self, producer, lvl):
        with open(producer + ".txt", 'r') as file:
            found = False
            for line in file:
                if found:
                    return line
                elif line.startswith("Production " + str(lvl)):
                    found = True
                    
                else:
                    pass
    def UpgradeBuilding(self, choice):
        import Main as M
        if choice == "1":
            self.HydroponicsLvl += 1
            self.HydroponicsProduction = self.GetProduction("Hydroponics", self.HydroponicsLvl)
        elif choice == "2":
            self.IHCLvl += 1
            self.IHCProduction = self.GetProduction("IHC", self.IHCLvl)
        elif choice == "3":
            self.ArbouretumLvl += 1
            self.ArbouretumProduction = self.GetProduction("Arbouretum", self.ArbouretumLvl)
        elif choice == "4":
            self.FusionReactorLvl += 1
            self.FusionReactorProduction = self.GetProduction("FusionReactor", self.FusionReactorLvl)
        elif choice == "5":
            self.CrewChambersLvl += 1
            self.CrewChambersProduction = self.GetProduction("CrewChambers", self.CrewChambersLvl)
        elif choice == "6":
            self.AMSLvl += 1
            self.AMSProduction = self.GetProduction("AMS", self.AMSLvl)
        elif choice == "7":
            self.HospitalLvl += 1
            self.HospitalProduction = self.GetProduction("Hospital", self.HospitalLvl)
        elif choice == "8":
            self.SpaLvl += 1
            self.SpaProduction = self.GetProduction("Spa", self.SpaLvl)
        self.update_text_file("MainBuildingFile.txt")
        PH.PrintHandler().FilePrint("BuildingsScreen.txt", False)
        self.BuildingScreen()

    def BuildingScreen(self):
        PH.PrintHandler().FilePrint("BuildingsScreen.txt", False)
        Choice = input()
        if Choice == "1":
            self.SpecificBuildingScreen("1")
        elif Choice == "2":
            self.SpecificBuildingScreen("2")
        elif Choice == "3":
            self.SpecificBuildingScreen("3")
        elif Choice == "4":
            self.SpecificBuildingScreen("4")
        elif Choice == "5":
            self.SpecificBuildingScreen("5")
        elif Choice == "6":
            self.SpecificBuildingScreen("6")
        elif Choice == "7":
            self.SpecificBuildingScreen("7")
        elif Choice == "8":
            self.SpecificBuildingScreen("8")
        else:
            print("Invalid choice. Please try again.")
            self.BuildingScreen(self)
