class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def _set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def _set_largeur(self, largeur):
        self.__largeur = largeur

    def afficher(self):
        print(f"Longueur: {self.__longueur}, Largeur: {self.__largeur}")

rectangle1 = Rectangle(10, 5)
rectangle1.afficher()
rectangle1._set_longueur(20)
rectangle1._set_largeur(10)
rectangle1.afficher()