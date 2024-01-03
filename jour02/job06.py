class Commande:
    def __init__(self, numero_commande, statut_commande="en cours"):
        self.__numero_commande = numero_commande
        self.__liste_plats_commandes = {}
        self.__statut_commande = statut_commande

    def ajouter_plat(self, plat, prix):
        self.__liste_plats_commandes[plat] = prix

    def annuler_commande(self):
        self.__statut_commande = "annulée"

    def __montant_commande(self):
        montant = 0
        for prix in self.__liste_plats_commandes.values():
            montant += prix
        return montant
    
    def __calculer_tva(self):
        return self.__montant_commande() * 0.2
    
    def afficher(self):
        print(f"Numéro de commande: {self.__numero_commande}")
        print(f"Statut de la commande: {self.__statut_commande}")
        print("Liste des plats commandés:")
        for plat, prix in self.__liste_plats_commandes.items():
            print(f"  {plat}: {prix} €") 
        print(f"Total à payer: {self.__montant_commande()} €")
        print(f"Montant de la TVA: {round(self.__calculer_tva(), 2)} €")

commande1 = Commande(1)
commande1.ajouter_plat("Pizza", 10)
commande1.ajouter_plat("Pâtes", 8)
commande1.ajouter_plat("Salade", 5)
commande1.afficher()