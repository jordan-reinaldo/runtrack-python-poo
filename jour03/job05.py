import random

class Personnage: 
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    def get_nom(self):
        return self.__nom
    
    def get_vie(self):
        return self.__vie
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_vie(self, vie):
        self.__vie = vie

    def recevoirDegats(self, degats):
        self.__vie -= degats
        self.__vie = max(self.__vie, 0)  # pour que la vie ne devienne pas négative

    def attaquer(self, ennemi):
        degats = random.randint(20, 50)
        ennemi.recevoirDegats(degats)


class Jeu:
    def __init__(self):
        self.__niveau = ""

    def choisirNiveau(self):
        self.__niveau = input("Choisissez un niveau de difficulté (facile, moyen ou difficile) : ")
        if self.__niveau not in ["facile", "moyen", "difficile"]:
            print("Erreur : niveau non reconnu.")
            self.choisirNiveau()

    def verifieVie(self, joueur, ennemi):
        while joueur.get_vie() > 0 and ennemi.get_vie() > 0:
            joueur.attaquer(ennemi)
            if ennemi.get_vie() > 0:
                ennemi.attaquer(joueur)

            print(f"{joueur.get_nom()} a {joueur.get_vie()} points de vie.")
            print(f"{ennemi.get_nom()} a {ennemi.get_vie()} points de vie.")
    
    def verifieVictoire(self, joueur, ennemi):
        if joueur.get_vie() > 0:
            print(f"{joueur.get_nom()} a gagné !")
        else:
            print(f"{ennemi.get_nom()} a gagné !")

    def lancerJeu(self):
        if self.__niveau == "facile":
            vie_joueur = vie_ennemi = 100
        elif self.__niveau == "moyen":
            vie_joueur = 95
            vie_ennemi = 120
        elif self.__niveau == "difficile":
            vie_joueur = 90
            vie_ennemi = 130
        else:
            print("Niveau non défini. Veuillez choisir un niveau.")
            return

        joueur = Personnage("Goku", vie_joueur)
        ennemi = Personnage("Vegeta", vie_ennemi)

        self.verifieVie(joueur, ennemi)
        self.verifieVictoire(joueur, ennemi)
        

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()