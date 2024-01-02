class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return round(prixTTC, 2)
    
    def CalculeTVA(self):
        coutTVA = self.prixHT * (self.TVA / 100)
        return f"Coût de la TVA: {round(coutTVA, 2)}€"
    
    def afficher(self):
        return(f"nom du produit: {self.nom}\nprixHT: {self.prixHT}€\n{self.CalculeTVA()} \nPrix TTC: {self.CalculerPrixTTC()}€")

    def modifier_nom(self, nom):
        self.nom = nom

    def modifier_prixHT(self, prixHT):
        self.prixHT = prixHT

    def afficher_nom(self):
        return(f"Le nom du produit est {self.nom}")

    def afficher_prixHT(self):
        return(f"Le prix HT du produit est {self.prixHT}€")

    def afficher_prixTTC(self):
        return(f"Le prix TTC du produit est {self.CalculerPrixTTC()}€")


chocolat = Produit("chocolat", 2, 20)
orange = Produit("Orange", 1, 20)

print(chocolat.afficher())
chocolat.modifier_nom("chocolat noir")
chocolat.modifier_prixHT(3)
print(chocolat.afficher_nom())
print(chocolat.afficher_prixHT())
print(chocolat.CalculeTVA())
print(chocolat.afficher_prixTTC())

print(orange.afficher())
orange.modifier_nom("Orange bio")
orange.modifier_prixHT(3.3)
print(orange.afficher_nom())
print(orange.afficher_prixHT())
print(orange.CalculeTVA())
print(orange.afficher_prixTTC())