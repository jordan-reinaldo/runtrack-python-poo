class Personnage : 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1
    
    def droite(self):
        self.x += 1

    def gauche(self):
        self.x -= 1

    def position(self):
        return(f"le personnage se trouve en {self.x} et {self.y}")
    

perso = Personnage()
print(perso.position())
perso.haut()
print(perso.position())
perso.bas()
print(perso.position())
perso.droite()
print(perso.position())
perso.gauche() 
print(perso.position())        
perso.gauche()
perso.bas() 
perso.bas()
print(perso.position())