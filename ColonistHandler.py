import os
import random
class ColonistHandler:
    def __init__(self, ID):
        print("ColonistHandler initialiazing...")
        if not os.path.exists(ID):
            self.create_text_file(ID)
        self.update_text_file(ID)


    def generate_new_colonist(self):
         Names = ["John", "Jane", "Jack", "Jim", "Jenny", "Joe", "Jill"]
         Name = random.choice(Names)
         Outlook = random.randint(1, 10)
         PossibleTraits = ["Brave", "Coward", "Lazy", "Hardworking", "Smart", "Dumb", "Kind", "Rude", "Honest", "Liar"]
         Trait = random.choice(PossibleTraits)
         Health = 100
         WorkSpeed = random.randint(1, 10)
         Hunger = random.randint(1, 10)
         return "" + "Name: " + str(Name) + "   " + "Outlook: " + str(Outlook) + "  " + "Trait: " + str(Trait) + "  " + "Health: " + str(Health) + "    " + "Work Speed: " + str(WorkSpeed) + "     " + "Hunger: " + str(Hunger) + ""
    
    def create_text_file(self, filename):
            with open(filename, 'w') as file:
                file.write("")
            print(f"File '{filename}' created successfully.")

    def update_text_file(self, filename):
        with open(filename, 'w') as file:
            file.write("" + self.generate_new_colonist() + "\n" + "\n" + self.generate_new_colonist() + "\n" + "\n" + self.generate_new_colonist() + "")
