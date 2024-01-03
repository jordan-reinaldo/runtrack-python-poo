class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__reservoir = reservoir
        self.__en_marche = False
    
    def get_marque(self):
        return self.__marque
    
    def __set_marque__(self, marque):
        self.__marque = marque
    
    def get_modele(self):
        return self.__modele

    def __set_modele__(self, modele):
        self.__modele = modele
    
    def get_annee(self):
        return self.__annee
    
    def __set_annee__(self, annee):
        self.__annee = annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def __set_kilometrage__(self, kilometrage):
        self.__kilometrage = kilometrage

    def demarrer(self):
        if self.__en_marche:
            print("La voiture est déjà en marche.")
        elif self.__reservoir > 5:
            self.__en_marche = True
            print("La voiture démarre.")
        else:    
            print("La voiture n'a pas assez d'essence pour démarrer.")

    def arreter(self):
        if self.__en_marche:
            self.__en_marche = False
            print("La voiture s'arrête.")
        else:
            print("La voiture est déjà à l'arrêt.")

    def verifier_plein(self):
        return self.__reservoir
    
Audi = Voiture("Audi", "A4", 2010, 100000, 100)
print(Audi.get_marque())
print(Audi.get_modele())
print(Audi.get_annee())
print(Audi.get_kilometrage())
Audi.demarrer()
Audi.arreter()