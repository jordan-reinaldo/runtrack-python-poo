class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est {self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def get_matiereEnseignee(self):
        return self.__matiereEnseignee
    
    def set_matiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

eleve = Eleve()
eleve.modifierAge(15)
eleve.bonjour()
eleve.allerEnCours()
eleve.afficherAge()

professeur = Professeur("FF14")
professeur.modifierAge(40)
professeur.bonjour()
professeur.enseigner()
professeur.afficherAge()