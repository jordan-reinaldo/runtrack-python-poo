class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.__marque}\nModèle : {self.__modele}\nAnnée : {self.__annee}\nPrix : {self.__prix} €")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)  
        self.__portes = portes

    def getPortes(self):
        return self.__portes
    
    def setPortes(self, portes):
        self.__portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()  
        print(f"Nombre de portes : {self.__portes}")

    def demarrer(self):
        print("Il faut que je démarre ma voiture, mais la voiture c'est nul")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix) 
        self.__roue = roue

    def getRoue(self):
        return self.__roue
    
    def setRoue(self, roue):
        self.__roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()  
        print(f"Nombre de roues : {self.__roue}")

    def demarrer(self):
        print("Je démarre ma moto car la moto c'est la vie et 100 fois mieux que la voiture !")

audi = Voiture("Audi", "A4", 2018, 20000)
audi.informationsVehicule()
audi.demarrer()

ktm_duke = Moto("KTM", "Duke", 2019, 5000)
ktm_duke.informationsVehicule()
ktm_duke.demarrer()