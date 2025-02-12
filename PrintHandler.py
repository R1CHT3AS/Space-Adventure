import os
class PrintHandler:
    
    def FilePrint(self, file, NoCenter):
        width = os.get_terminal_size().columns
        with open(file, 'r', encoding='utf-8') as f:
            if NoCenter == True:
                for line in f:
                    print(line.rstrip())
            else:
                for line in f:
                    print(line.rstrip().center(width))
                
                