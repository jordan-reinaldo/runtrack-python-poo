class Student: 
    def __init__(self, nom, prenom, numero_etudiant, credits=0): 
        self.__nom = nom
        self.__prenom = prenom  
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval__()
     
    def get_credit(self):
        return f"Le nombre de crédits de {self.__prenom} {self.__nom} est de {self.__credits}"

    def __add_credits__(self, credits): 
        if credits > 0: 
            self.__credits += credits
            self.__level = self.__studentEval__()
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à 0.")

    def __studentEval__(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return  "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:   
            return "Insuffisant"
        
    def studentInfo(self):
        print(f"Nom: {self.__nom} \nPrénom: {self.__prenom} \nId: {self.__numero_etudiant} \nCrédits: {self.__credits} \nNiveau: {self.__level}")

john = Student("Doe", "John", 145, 0)

print(john.get_credit())
john.__add_credits__(40)
john.__add_credits__(30)
john.__add_credits__(30)
print(john.get_credit())
print(john.__studentEval__())
john.studentInfo()