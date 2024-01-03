class Commande:
    
    menu = {
        "Pizza Armenienne": 14.5,
        "Coca-Cola": 2.5,
        "Spaghetti Bolognaise": 15.0,
        "Salade César": 10.0,
        "Tiramisu": 7.5,
        "Eau": 1.5,
        "Café": 1.0,
        "Thé": 1.0,
    }

    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {} 
        self.__statut = "en cours"
    
    def ajouter_plat(self, nom_plat, quantite=1):
        if nom_plat in Commande.menu:
            if nom_plat not in self.__plats_commandes:
                self.__plats_commandes[nom_plat] = quantite
            else:
                self.__plats_commandes[nom_plat] += quantite
        else:
            print(f"Le plat '{nom_plat}' n'est pas disponible dans le menu.")

    def annuler_commande(self):
        self.__statut = "annulée"
        self.__plats_commandes.clear()
    
    def payer(self):
        self.__statut = "terminée"
        self.__plats_commandes.clear()

    def __calculer_total(self):
        return sum(Commande.menu[plat] * quantite for plat, quantite in self.__plats_commandes.items())

    def __calculer_TVA(self, taux_tva):
        total = self.__calculer_total()
        return total * taux_tva / 100

    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande N°{self.__numero_commande}")
        print(f"Statut de la commande: {self.__statut}")
        for plat, quantite in self.__plats_commandes.items():
            prix = Commande.menu[plat]
            print(f"{plat}: {prix}€ x {quantite}")
        print(f"Total à payer: {total}€")
        print(f"TVA : {commande.__calculer_TVA(10)}€")

    

commande = Commande(1)
commande.ajouter_plat("Pizza Armenienne", 2)
commande.ajouter_plat("Coca-Cola", 3)
commande.ajouter_plat("Spaghetti Bolognaise", 1)
commande.ajouter_plat("Salade César", 1)
commande.afficher_commande()
commande.payer()
commande.afficher_commande()