import os
class PrintHandler:
    
    def FilePrint(self, file):
        width = os.get_terminal_size().columns
        with open(file, 'r') as f:
            for line in f:
                print(line.rstrip().center(width))
                