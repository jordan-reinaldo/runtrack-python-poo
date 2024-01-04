class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = True

    def get_numero_compte(self):
        return self.__numero_compte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def set_numero_compte(self, numero_compte):
        self.__numero_compte = numero_compte

    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_solde(self, solde):
        self.__solde = solde
    
    def afficher(self):
        print(f"Numéro de compte: {self.__numero_compte}, Nom: {self.__nom}, Prénom: {self.__prenom}, Solde: {self.__solde}")

    def afficherSolde(self):
        print(f"Le solde du compte {self.__numero_compte} est de {self.__solde} euros.")

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            self.afficherSolde()
        else:
            print("Erreur : Le montant doit être supérieur à 0.")

    def retrait(self, montant):
        if self.__solde - montant < 0 and self.__decouvert==False:
            print("Erreur : Le solde du compte ne peut pas être négatif.")
        elif montant > 0:
            self.__solde -= montant
            self.afficherSolde()
        else:
            print("Erreur : Le montant doit être supérieur à 0.")

    def agios(self, taux):
        self.__solde -= self.__solde * taux / 100
        self.afficherSolde()
 

    def virement(self, montant, compte):
        if self.__solde - montant < 0 and self.__decouvert==False:
            print("Erreur : Le solde du compte ne peut pas être négatif.")
        elif montant > 0:
            self.__solde -= montant
            compte.__solde += montant
            self.afficherSolde()
        else:
            print("Erreur : Le montant doit être supérieur à 0.")

    def autorisationDecouvert(self):
        self.__decouvert = True

    def refusDecouvert(self):
        self.__decouvert = False

compte1 = CompteBancaire(123456789, "Doe", "John", 1000)
compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(100)
compte1.afficher()

compte2 = CompteBancaire(987654321, "Zinedine", "Zidan", -500)
compte2.afficher()
compte2.agios(10)
compte1.virement(450, compte2)
compte2.afficher()