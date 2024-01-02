class operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        return self.nombre1 + self.nombre2

exemple = operation(10, 12)

print(f" le nombre 1 est {exemple.nombre1}")
print(f" le nombre 2 est {exemple.nombre2}")
print(f" nombre1 + nombre2 = {exemple.addition()}")