class Forme:

    def aire(self):
        self.aire = 0 
        return self.aire
    
class Cercle(Forme):

    def __init__(self, rayon):
        self.__rayon = rayon

    def getRayon(self):
        return self.__rayon
    
    def setRayon(self, rayon):
        self.__rayon = rayon

    def aire(self):
        self.aire =  self.__rayon * self.__rayon * 3.14
        return self.aire
    
cercle1 = Cercle(10)
print(f"L'aire du cercle est : {cercle1.aire()}")