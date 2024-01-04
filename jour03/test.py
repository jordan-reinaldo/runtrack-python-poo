class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde,):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = True

    def _getNumeroCompte(self):
        return self.__numero_compte
    
    def _getNom(self):
        return self.__nom
    
    def _getPrenom(self):
        return self.__prenom
    
    def _getSolde(self):
        return self.__solde
    
    def _setNumeroCompte(self, numero_compte):
        self.__numero_compte = numero_compte

    def _setNom(self, nom):
        self.__nom = nom

    def _setPrenom(self, prenom):
        self.__prenom = prenom

    def _setSolde(self, solde):
        self.__solde = solde

    def _afficher(self):
        print(f'Le compte numéro {self.__numero_compte} appartient à {self.__prenom} {self.__nom}.')

    def _afficherSolde(self):
        print(f'Le solde du compte numéro {self.__numero_compte} est de {self.__solde} euros')

    def _versement(self, montant):
        self.__solde += montant

    def _retrait(self, somme):
        if self.__solde - somme < 0 and self.__decouvert==False:
            print("Erreur : Le solde du compte ne peut pas être négatif.")
        elif somme > 0:
            self.__solde -= somme
            self._afficherSolde()
        else:
            print("Erreur : Le montant doit être supérieur à 0.")

    def _agios(self):
        if self.__solde < 0:
            self.__solde *= 1.05

    def virement(self, compte_destinataire, montant):
        if self.solde - montant < 0 and not self.decouvert:
            print("Opération impossible, le solde ne peut pas être négatif.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
            self.afficherSolde()
            compte_destinataire.afficherSolde()

compte1 = CompteBancaire(25, "Dupont", "Jean", 250000)
compte1._afficher()
compte1._afficherSolde()
compte1._versement(500)
compte1._afficherSolde()
compte1._retrait(1500)
compte1._afficherSolde()
print("\n")
compte2 = CompteBancaire(13, "Vaisse", "Maxence", -10000)
compte2._afficher()
compte2._afficherSolde()
compte1._virement(compte2, 1000)