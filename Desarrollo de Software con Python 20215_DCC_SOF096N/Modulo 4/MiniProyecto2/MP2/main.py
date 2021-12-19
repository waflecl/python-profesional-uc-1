import parametros as p
import random

###### INICIO PUNTO 1 ######
### Rellenar Clase Automóvil ###
class Automovil:
    pass
###### FIN PUNTO 1 ######


###### INICIO PUNTO 2 ######
### Rellenar Clase Moto ###
class Moto: 
    pass

    def __str__(self):
        return f"Moto del año {self.ano}."
###### FIN PUNTO 2 ######


###### INICIO PUNTO 3 ######
### Rellenar Clase Camión ###
class Camion:
    pass

    def __str__(self):
        return f"Camión del año {self.ano}."
###### FIN PUNTO 3 ######


### Esta clase está completa, NO MODIFICAR ###
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia
        self.estado = "Perfecto"

    def gastar(self, accion):
        if accion == "acelerar":
            resistencia_actual -= 5
        elif accion == "frenar":
            resistencia_actual -= 10
        self.actualizar_estado()

    def actualizar_estado(self):
        if resistencia_actual < 0:
            self.estado = "Rota"
        elif resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif resistencia_actual < self.resistencia_total:
            self.estado = "Usada"

### Esta funcion está completa, NO MODIFICAR ###
def seleccionar():
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    if elegido >= 0 and elegido < len(vehiculos):
        vehiculo = vehiculos[elegido]
        print("Se seleccionó el vehículo", str(vehiculo))
    else:
        print("intentelo denuevo.")


###### INICIO PUNTO 4.2 ######
### Se debe completar cada opción según lo indicado en el enunciado ###
def accion(vehiculo, opcion):
    if opcion == 2: #Acelerar
        pass
    elif opcion == 3: #Frenar
        pass
    elif opcion == 4: #Avanzar
        pass
    elif opcion == 5: #Cambiar Rueda
        pass
    elif opcion == 6: #Mostrar Estado
        pass 
###### FIN PUNTO 4.2 ######


if __name__ == "__main__":

    ###### INICIO PUNTO 4.1 ######
    ### Aca deben instanciar los vehiculos indicados
    ### en el enunciado y agregarlos a la lista vehiculos
    vehiculos = []


    ###### FIN PUNTO 4.1 ######


    ### El codigo de abajo NO SE MODIFICA ###
    vehiculo = vehiculos[0] # Por default comienza seleccionado el primer vehículo  

    dict_opciones = {1: ("Seleccionar Vehiculo", seleccionar),
                     2: ("Acelerar", accion),
                     3: ("Frenar", accion),
                     4: ("Avanzar", accion),
                     5: ("Reemplazar Rueda", accion),
                     6: ("Mostrar Estado", accion),
                     0: ("Salir", None)
                    }

    op = -1
    while op != 0:
        
        for k, v in dict_opciones.items():
            print(f"{k}: {v[0]}")
        
        try:
            op = int(input("Opción: "))
        
        except ValueError:
            print(f"Ingrese opción válida.")
            op = -1
        
        if op != 0 and op in dict_opciones.keys():
            if op == 1:
                dict_opciones[op][1]()
            else:
                dict_opciones[op][1](vehiculo, op)
        elif op == 0:
            pass
        else:
            print(f"Ingrese opción válida.")
            op = -1
