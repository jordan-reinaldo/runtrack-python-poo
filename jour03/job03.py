class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "à faire"

    def get_titre(self):
        return self.__titre

    def get_description(self):
        return self.__description

    def get_statut(self):
        return self.__statut

    def set_titre(self, titre):
        self.__titre = titre

    def set_description(self, description):
        self.__description = description

    def set_statut(self, statut):
        self.__statut = statut


class ListeDeTaches:
    def __init__(self):
        self.__liste = []

    def ajouterTache(self, tache):
        self.__liste.append(tache)

    def supprimerTache(self, tache):
        self.__liste.remove(tache)

    def afficherListe(self):
        resultat = ""
        for tache in self.__liste:
            resultat += f"{tache.get_titre()}: {tache.get_description()}, Statut: {tache.get_statut()}\n"
        return resultat.strip()

    def filtrerListe(self):
        resultat = ""
        for tache in self.__liste:
            if tache.get_statut() == "à faire":
                resultat += f"{tache.get_titre()}: {tache.get_description()}, Statut: {tache.get_statut()}\n"
        return resultat.strip()


    def marquerCommeFinie(self, tache):
        tache.set_statut("terminée")


liste_taches = ListeDeTaches()

tache1 = Tache("Faire les courses", "Acheter du pain, du lait et des oeufs")
tache2 = Tache("Aller à la piscine", "Nager 20 longueurs")
tache3 = Tache("Faire du sport", "Courir 30 minutes")

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)
print(f"Liste des tâches :\n{liste_taches.afficherListe()}")

liste_taches.supprimerTache(tache3)
print(f"Liste des tâches :\n{liste_taches.afficherListe()}")

liste_taches.marquerCommeFinie(tache2)
print(f"Liste des tâches :\n{liste_taches.afficherListe()}")

print(f"Liste des tâches à faire :\n{liste_taches.filtrerListe()}")