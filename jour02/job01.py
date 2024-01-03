class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def __set_longueur__(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur

    def __set_largeur__(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    def afficher(self):
        print(f"Longueur: {self.__longueur}, Largeur: {self.__largeur}")

rectangle1 = Rectangle(10, 5)
rectangle1.afficher()
rectangle1.__set_longueur__(20)
rectangle1.__set_largeur__(10)
rectangle1.afficher()