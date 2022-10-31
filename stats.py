from rich import print

class Statystyki():
    def __init__(self, przedmioty=2, upojenie = 0):
        self.przedmioty = 2
        self.upojenie = 0
        
    def get_przedmioty(self):
        return self.przedmioty
    
    def set_przedmioty(self, przedmioty = 2):
        self.przedmioty = przedmioty
        
    def set_upojenie(self):
        self.upojenie = 0
        
    def get_upojenie(self):
        return self.upojenie
        
    def niezdal(self):
        self.przedmioty -= 1
    
    def pije(self):
        self.upojenie += 1
        
    def printupojenie(self):
        print("[green]Poziom upojenia Adama: " + str(self.upojenie) + "/5.")
        
    def printstats(self):
        print("[yellow]Dopuszczalne negatywne oceny w roku: " + str(self.przedmioty) + "/2.")
         

