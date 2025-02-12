import os
import PrintHandler as PH
class ResourceHandler:
    def __init__(self, ID):
        print("ResourceHandler initialiazing...")
        self.Oxy = 0
        self.Hyd = 0
        self.Ele = 0
        self.Foo = 0
        self.Alo = 0
        if not os.path.exists(ID):
            self.create_text_file(ID)
        self.update_text_file(ID)



    
    def create_text_file(self, filename):
            with open(filename, 'w') as file:
                file.write("")
            print(f"File '{filename}' created successfully.")

    def update_text_file(self, filename):
        with open(filename, 'w') as file:
            file.write("Oxygen = " + str(self.Oxy) + "\n" + "Hydrogen = " + str(self.Hyd) + "\n" + "Electricity = " + str(self.Ele) + "\n" + "Food = " + str(self.Foo) + "\n" + "Alloys = " + str(self.Alo))




