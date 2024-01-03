class Livre:

    def __init__(self, auteur, titre, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, nouveau_titre): 
        self.__titre = nouveau_titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, nouveau_auteur):  
        self.__auteur = nouveau_auteur 
    
    def get_pages(self):
        return self.__pages
    
    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0: #vérifie si la variable pages est une instance de la classe int (si c'est un entier)
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher(self):
        print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Pages: {self.__pages}")

Livre1 = Livre("Victor Hugo", "Les Misérables", 1488)
Livre1.afficher()
Livre1.set_titre("Harry Potter")
Livre1.set_auteur("J.K. Rowling")
Livre1.set_pages(-1)
Livre1.afficher()