class Student: 
    def __init__(self, nom, prenom, numero_etudiant, credits=0): 
        self.__nom = nom
        self.__prenom = prenom  
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()
     
    def get_credit(self):
        return f"Le nombre de crédits de {self.__prenom} {self.__nom} est de {self.__credits}"

    def _add_credits(self, credits): 
        if credits > 0: 
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à 0.")

    def __studentEval(self):
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
        print(f"Nom: {self.__nom} \nPrénom: {self.__prenom} \nId: {self.__numero_etudiant}\nNiveau: {self.__level}")

john = Student("Doe", "John", 145, 0)

print(john.get_credit())
john._add_credits(40)
john._add_credits(30)
john._add_credits(30)
print(john.get_credit())
john.studentInfo()