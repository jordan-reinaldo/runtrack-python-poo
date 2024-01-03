class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    def afficher(self):
        print(f"Longueur: {self.__longueur}, Largeur: {self.__largeur}")

rectangle1 = Rectangle(10, 5)
rectangle1.afficher()
rectangle1.set_longueur(20)
rectangle1.set_largeur(10)
rectangle1.afficher()