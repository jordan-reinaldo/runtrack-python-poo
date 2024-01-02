class Animal : 
    def __init__(self,age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

luna = Animal()

print(f"l'age de l'animal est {luna.age} ans")
luna.vieillir()
print(f"l'age de l'animal est {luna.age} ans")
luna.nommer("Luna")
print(f"L'animal se nomme {luna.prenom}")