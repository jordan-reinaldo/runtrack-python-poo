class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return(f"le point a pour coordonnées {self.x} et {self.y}")

    def afficherX(self):
        return(f"le point a pour coordonnée x {self.x}")
    
    def afficherY(self):
        return(f"le point a pour coordonnée y {self.y}")
    
    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y

exemple = Point(10, 12)

print(exemple.afficherLesPoints())
print(exemple.afficherX())
print(exemple.afficherY())
exemple.changerX(15)
print(exemple.afficherX())
exemple.changerY(20)
print(exemple.afficherY())