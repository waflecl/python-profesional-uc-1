class Persona:

    def __init__(self, nombre, apellido, rut, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.edad = edad
    
    def __str__(self):
        return "Soy {} {} y mi RUT es {} y tengo {} años".format(self.nombre, self.apellido, self.rut, self.edad)
    
    def cumpleaños(self):
        self.edad += 1
    
    def getRut(self):
        return self.rut

if __name__ == "__main__":
    persona = Persona("Juan", "Perez", "12345678-9", 20)
    print(persona)
    persona.cumpleaños()
    print(persona)
    print(persona.getRut())