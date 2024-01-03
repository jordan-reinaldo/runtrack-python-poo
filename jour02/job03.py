class Livre:

    def __init__(self, auteur, titre, pages):
        self.__titre = titre
        self.__auteur = auteur
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")
            self.__pages = "nombre de pages incorrect"
        self.__disponible = True

    def get_titre(self):
        return self.__titre
    
    def __set_titre__(self, nouveau_titre): 
        self.__titre = nouveau_titre
    
    def get_auteur(self):
        return self.__auteur
    
    def __set_auteur__(self, nouveau_auteur):  
        self.__auteur = nouveau_auteur 
    
    def get_pages(self):
        return self.__pages
    
    def __set_pages__(self, pages):
        if isinstance(pages, int) and pages > 0: #vérifie si la variable pages est une instance de la classe int (si c'est un entier)
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher(self):
        print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Pages: {self.__pages}")

    def __vérification__(self):
        return self.__disponible

    def emprunter(self):
        if self.__vérification__():  
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible car il a déjà été emprunté.")

    def rendre(self):
        if not self.__vérification__():  
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

livre1 = Livre("Victor Hugo", "Les Misérables", 1488)
livre1.afficher()
livre1.emprunter()
livre1.rendre()
livre1.emprunter()
livre1.emprunter()