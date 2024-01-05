import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    valeurs = [str(n) for n in range(2, 11)] + ["Valet", "Dame", "Roi", "As"]
    couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]

    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for couleur in self.couleurs for valeur in self.valeurs]
        self.main_joueur = []
        self.main_croupier = []
        self.melanger()

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

    def distribuer(self):
        for _ in range(2):
            self.main_joueur.append(self.tirer_carte())
            self.main_croupier.append(self.tirer_carte())

    def afficher_main(self, main):
        return ', '.join(map(str, main))

    def calculer_score(self, main):
        score = 0
        as_compte = 0
        for carte in main:
            if carte.valeur in ["Valet", "Dame", "Roi"]:
                score += 10
            elif carte.valeur == "As":
                as_compte += 1
                score += 11
            else:
                score += int(carte.valeur)
        while score > 21 and as_compte:
            score -= 10
            as_compte -= 1
        return score

    def jouer_tour_joueur(self):
        choix = input("Voulez-vous prendre une carte ? (oui/non): ").lower()
        while choix == "oui":
            self.main_joueur.append(self.tirer_carte())
            print("Votre main : ", self.afficher_main(self.main_joueur))
            print("Main du croupier : ", self.afficher_main(self.main_croupier))
            if self.calculer_score(self.main_joueur) > 21:
                print("Vous avez dépassé 21, vous avez perdu !")
                return False
            choix = input("Voulez-vous prendre une carte ? (oui/non): ").lower()
        print("Votre main finale : ", self.afficher_main(self.main_joueur))
        print("Main finale du croupier : ", self.afficher_main(self.main_croupier))
        return True

    def jouer_tour_croupier(self):
        while self.calculer_score(self.main_croupier) < 17:
            self.main_croupier.append(self.tirer_carte())
            print("Main du croupier: ", self.afficher_main(self.main_croupier))

    def verifier_victoire(self):
        score_joueur = self.calculer_score(self.main_joueur)
        score_croupier = self.calculer_score(self.main_croupier)
        print("Votre score:", score_joueur)
        print("Score du croupier:", score_croupier)
        if score_joueur > 21:
            print("Vous avez perdu !")
        elif score_croupier > 21 or score_joueur > score_croupier:
            print("Vous avez gagné !")
        else:
            print("Le croupier gagne.")

jeu = Jeu()
jeu.distribuer()
print("Votre main initiale:", jeu.afficher_main(jeu.main_joueur))
print("Main initiale du croupier:", jeu.afficher_main(jeu.main_croupier))
if jeu.jouer_tour_joueur():
    jeu.jouer_tour_croupier()
    jeu.verifier_victoire()