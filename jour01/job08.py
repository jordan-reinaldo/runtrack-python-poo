class Cercle :
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon

    def aire(self):
        return self.rayon**2*3.14 

    def circonference(self):
        return self.rayon*2*3.14 
    
    def diametre(self):
        return self.rayon*2
    
    def afficherInfos(self):
        print(f"le rayon est {self.rayon}")
        print(f"l'aire est {self.aire()}")
        print(f"la circonference est {self.circonference()}")
        print(f"le diametre est {self.diametre()}")

cercle1 = Cercle(4)
cercle1.afficherInfos()
cercle1.changerRayon(10)
cercle1.afficherInfos()

cercle2 = Cercle(7)
cercle2.afficherInfos()
cercle2.changerRayon(12)
cercle2.afficherInfos()