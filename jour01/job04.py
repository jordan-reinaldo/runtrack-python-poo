class personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f"je suis {self.prenom} {self.nom}")


Jordan = personne("Reinaldo", "Jordan")
Jennifer = personne("Tovar", "Jennifer")

Jordan.SePresenter()
Jennifer.SePresenter()