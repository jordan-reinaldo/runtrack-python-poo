class Joueur: 
    def __init__(self, nom, numero, position, nombre_but_marques, passes_decisives, carton_jaune, carton_rouge):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__nombre_but_marques = nombre_but_marques
        self.__passes_decisives = passes_decisives
        self.__carton_jaune = carton_jaune
        self.__carton_rouge = carton_rouge
       
    def get_nom(self):
        return self.__nom
    
    def get_numero(self):
        return self.__numero
    
    def get_position(self):
        return self.__position
    
    def get_nombre_but_marques(self):
        return self.__nombre_but_marques
    
    def get_passes_decisives(self):
        return self.__passes_decisives
    
    def get_carton_jaune(self): 
        return self.__carton_jaune
    
    def get_carton_rouge(self):
        return self.__carton_rouge
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_numero(self, numero):
        self.__numero = numero

    def set_position(self, position):
        self.__position = position

    def set_nombre_but_marques(self, nombre_but_marques):
        self.__nombre_but_marques = nombre_but_marques

    def set_passes_decisives(self, passes_decisives):
        self.__passes_decisives = passes_decisives

    def set_carton_jaune(self, carton_jaune):
        self.__carton_jaune = carton_jaune

    def set_carton_rouge(self, carton_rouge):
        self.__carton_rouge = carton_rouge

    def marquerUnBut(self):
        self.__nombre_but_marques += 1

    def faireUnePasseDecisive(self):
        self.__passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.__carton_jaune += 1

    def recevoirUnCartonRouge(self):
        self.__carton_rouge += 1

    def afficherStatistiques(self):
        return (f"Nom Joueur: {self.__nom}\n"
                f"Numéro: {self.__numero}\n"
                f"Position: {self.__position}\n"
                f"Nombre de Buts: {self.__nombre_but_marques}\n"
                f"Passes Décisives: {self.__passes_decisives}\n"
                f"Cartons Jaunes: {self.__carton_jaune}\n"
                f"Cartons Rouges: {self.__carton_rouge}\n")


class Equipe: 
    def __init__(self, nom, ListeJoueur):
        self.__nom = nom
        self.__ListeJoueur = ListeJoueur

    def ajouterJoueur(self, joueur):
        self.__ListeJoueur.append(joueur)

    def AfficherStatistiquesDesJoueurs(self):
        print(f"Statistiques de l'équipe: {self.__nom}\n")
        for joueur in self.__ListeJoueur:
            print(joueur.afficherStatistiques())

    def mettreAJourStatisquesJoueur(self, nom, nombre_but_marques, passes_decisives, carton_jaune, carton_rouge):
        for joueur in self.__ListeJoueur:
            if joueur.get_nom() == nom:
                joueur.set_nombre_but_marques(nombre_but_marques)
                joueur.set_passes_decisives(passes_decisives)
                joueur.set_carton_jaune(carton_jaune)
                joueur.set_carton_rouge(carton_rouge)


kanou = Joueur("Kanou", 9, "Attaquant", 9, 3, 1, 0)
zidane = Joueur("Zidane", 10, "Milieu", 3, 6, 1, 2)
ronaldo = Joueur("Ronaldo", 7, "Attaquant", 5, 2, 2, 0)
messi = Joueur("Messi", 10, "Attaquant", 4, 4, 0, 0)
casillas = Joueur("Casillas", 1, "Gardien", 0, 0, 0, 0)
om = Equipe("OM", [])

om.ajouterJoueur(kanou)
om.ajouterJoueur(zidane)
om.ajouterJoueur(ronaldo)
om.ajouterJoueur(messi)
om.ajouterJoueur(casillas)
om.AfficherStatistiquesDesJoueurs()


jordan = Joueur("Jordan", 23, "Attaquant", 9, 3, 1, 0)
maxence = Joueur("Maxence", 10, "Milieu", 3, 6, 1, 2)
rheda = Joueur("Rheda", 7, "Attaquant", 5, 2, 2, 0)
rija = Joueur("Rija", 10, "Defenseur", 4, 4, 0, 0)
jean = Joueur("Jean", 1, "Gardien", 0, 0, 0, 0)
laplateforme = Equipe("LaPlateforme", [])

laplateforme.ajouterJoueur(jordan)
laplateforme.ajouterJoueur(maxence)
laplateforme.ajouterJoueur(rheda)
laplateforme.ajouterJoueur(rija)
laplateforme.ajouterJoueur(jean)
laplateforme.AfficherStatistiquesDesJoueurs()

jordan.marquerUnBut()
rheda.faireUnePasseDecisive()
jordan.recevoirUnCartonJaune()
rija.recevoirUnCartonRouge()
zidane.recevoirUnCartonRouge()
laplateforme.AfficherStatistiquesDesJoueurs()
om.AfficherStatistiquesDesJoueurs()
laplateforme.mettreAJourStatisquesJoueur("Jordan", 30, 5, 2, 1)
print(jordan.afficherStatistiques())