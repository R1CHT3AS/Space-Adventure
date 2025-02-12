import os
class BuildingsHandler:
    def __init__(self, ID):
        print("BuildingHandler initialiazing...")
        self.HydroponicsLvl = 1
        self.IHCLvl = 1
        self.ArbouretumLvl = 1
        self.FusionReactorLvl = 1
        self.CrewChambersLvl = 1
        self.AMSLvl = 1
        self.HospitalLvl = 1
        self.SpaLvl = 1
        if not os.path.exists(ID):
            self.create_text_file(ID)
        self.update_text_file(ID)
    
    def create_text_file(self, filename):
            with open(filename, 'w') as file:
                file.write("")
            print(f"File '{filename}' created successfully.")

    def update_text_file(self, filename):
        with open(filename, 'w') as file:
            file.write("Hydroponics Level = " + str(self.HydroponicsLvl) + "\n" + "Ice Harvesting Center Level = " + str(self.IHCLvl) + "\n" + "Arbouretum Level = " + str(self.ArbouretumLvl) + "\n" + "Fusion Reactor Level = " + str(self.FusionReactorLvl) + "\n" + "Crew Chambers Level = " + str(self.CrewChambersLvl) + "\n" + "Atmosphere Management System Level = " + str(self.AMSLvl) + "\n" + "Hospital Level = " + str(self.HospitalLvl) + "\n" + "Spa Level = " + str(self.SpaLvl))