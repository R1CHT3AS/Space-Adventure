import PrintHandler as PH
class ScreenHandler:
    def __init__(self, ID):
        pass

        

    def OpenScreen(self, screen, ID):
        PH.PrintHandler().FilePrint(screen)
        with open(ID, 'r') as f:
            for line in f:
                print(line(1, 10))