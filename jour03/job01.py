class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom
    
    def get_nombre_habitants(self):
        return self.__nombre_habitants
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_nombre_habitants(self, nombre_habitants):
        self.__nombre_habitants = nombre_habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    def set_nom(self, nom):
        self.__nom = nom

    def ajouterPopulation(self):
        self.__ville.set_nombre_habitants(self.__ville.get_nombre_habitants() + 1)

paris = Ville("Paris", 1000000)
print(f"le nombre d'habitant de {paris.get_nom()} est de:{paris.get_nombre_habitants()}")

marseille = Ville("Marseille", 861635)
print(f"le nombre d'habitant de {marseille.get_nom()} est de:{marseille.get_nombre_habitants()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouterPopulation()
print(f"Le nombre d'habitant de la ville de {paris.get_nom()} est maintenant de :{paris.get_nombre_habitants()}")
myrtille.ajouterPopulation()
print(f"Le nombre d'habitant de la ville de {paris.get_nom()} est maintenant de :{paris.get_nombre_habitants()}")
chloe.ajouterPopulation()
print(f"Le nombre d'habitant de la ville de {marseille.get_nom()} est maintenant de :{marseille.get_nombre_habitants()}")