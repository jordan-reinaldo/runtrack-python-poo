class Forme:

    def aire(self):
        self.aire = 0 
        return self.aire
    
class Rectangle(Forme):

    def __init__(self, hauteur, largeur):
        self.__hauteur = hauteur
        self.__largeur = largeur

    def getHauteur(self):
        return self.__hauteur
    
    def getLargeur(self):
        return self.__largeur
    
    def setHauteur(self, hauteur):
        self.__hauteur = hauteur

    def setLargeur(self, largeur):
        self.__largeur = largeur

    def aire(self):
        self.aire =  self.__hauteur * self.__largeur
        return self.aire

rectangle1 = Rectangle(12, 7)

print(f"L'aire du rectangle est : {rectangle1.aire()}")