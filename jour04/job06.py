class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix

    def getMarque(self):
        return self.__marque
    
    def getModele(self):
        return self.__modele
    
    def getAnnee(self):
        return self.__annee
    
    def getPrix(self):
        return self.__prix
    
    def setMarque(self, marque):
        self.__marque = marque

    def setModele(self, modele):
        self.__modele = modele

    def setAnnee(self, annee):
        self.__annee = annee

    def setPrix(self, prix):
        self.__prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.__marque}\nModèle : {self.__modele}\nAnnée : {self.__annee}\nPrix : {self.__prix} €")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, portes=4):
        self.__portes = portes

    def getPortes(self):
        return self.__portes
    
    def setPortes(self, portes):
        self.__portes = portes

    def informationsVehicule(self):
        print(f"Marque : {self.getMarque()}\nModèle : {self.getModele()}\nAnnée : {self.getAnnee()}\nPrix : {self.getPrix()}\nNombre de portes : {self.getPortes()}")

    def demarrer(self):
        print("il faut que je demarre ma voiture mais la voiture c'est nul")

class Moto(Vehicule):
    def __init__(self, roue=2):
        self.__roue = roue

    def getRoue(self):
        return self.__roue
    
    def setRoue(self, roue):
        self.__roue = roue

    def informationsVehicule(self):
        print(f"Marque : {self.getMarque()}\nModèle : {self.getModele()}\nAnnée : {self.getAnnee()}\nPrix : {self.getPrix()}\nNombre de roues : {self.getRoue()}")

    def demarrer(self):
        print("Je demarre ma moto car la moto c'est la vie et 100 fois mieux que la voiture !")


audi = Voiture()
audi.setMarque("Audi")
audi.setModele("A3")
audi.setAnnee(2019)
audi.setPrix(25000) 
audi.informationsVehicule()
audi.demarrer()

ktm_duke = Moto()
ktm_duke.setMarque("KTM")
ktm_duke.setModele("Duke")
ktm_duke.setAnnee(2018)
ktm_duke.setPrix(5000)
ktm_duke.informationsVehicule()
ktm_duke.demarrer()