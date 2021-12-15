class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

def cambiar(persona_1, persona_2):
    nom = persona_1.nombre
    persona_1.nombre = persona_2.nombre
    persona_2.nombre = nom

if __name__ == "__main__":
    persona_1 = Persona("Juan")
    persona_2 = Persona("Diego")
    cambiar(persona_1, persona_2)
    print(persona_1.nombre)
    print(persona_2.nombre)