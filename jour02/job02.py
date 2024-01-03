class Livre:

    def __init__(self, auteur, titre, pages):
        self.__titre = titre
        self.__auteur = auteur
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")
            self.__pages = "nombre de pages incorrect"

    def get_titre(self):
        return self.__titre
    
    def _set_titre(self, nouveau_titre): 
        self.__titre = nouveau_titre
    
    def get_auteur(self):
        return self.__auteur
    
    def _set_auteur(self, nouveau_auteur):  
        self.__auteur = nouveau_auteur 
    
    def get_pages(self):
        return self.__pages
    
    def _set_pages(self, pages):
        if isinstance(pages, int) and pages > 0: #vérifie si la variable pages est une instance de la classe int (si c'est un entier)
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher(self):
        print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Pages: {self.__pages}")

livre1 = Livre("Victor Hugo", "Les Misérables", 1488)
livre1.afficher()
livre1._set_titre("Harry Potter")
livre1._set_auteur("J.K. Rowling")
livre1._set_pages(500)
livre1.afficher()