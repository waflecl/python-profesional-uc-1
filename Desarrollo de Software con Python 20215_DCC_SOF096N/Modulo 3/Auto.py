class Auto:
    def __init__(self, ma, mo, a, c, k):
        self.marca = ma
        self.modelo = mo
        self.año = a
        self.color = c
        self.__kilometraje = k
        self.__ubicacion = (-33.45, -70.66)
        self.dueño = None
    
    def __str__(self):
        return f"Auto de {self.dueño}, Modelo: {self.modelo}, año: {self.año}, {self.__kilometraje} kms, Color: {self.color}"
    
    def conducir(self, kms):
        self.__kilometraje += kms
        self.__modificar_ubicacion(kms/20, kms/30)
    
    def vender(self, dueño):
        self.dueño = dueño
    
    def leer_odometro(self):
        return self.__kilometraje
    
    def __modificar_ubicacion(self, dlat, dlon):
        print("Modificando ubicación...")
        self.__ubicacion = (self.__ubicacion[0] + dlat, self.__ubicacion[1] + dlon)

if __name__ == "__main__":
    a = Auto("Ford", "Fiesta", 2015, "Azul", 100)
    b = Auto("Chevrolet", "Camaro", 2018, "Rojo", 200)

    print(a)
    print(b)

    a.vender("Juan")
    b.vender("Pedro")

    a.conducir(100)
    b.conducir(200)

    print(a)
    print(b)

    b.color = "Verde"
    print(b)

    b.__kilometraje = 1000
    print(b)

    b.conducir(10000)
    print(b)