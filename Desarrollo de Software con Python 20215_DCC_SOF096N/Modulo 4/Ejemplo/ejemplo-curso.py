class Curso:
    
    def __init__(self, nombre, año, semestre, creditos, minimo):
        self.nombre = nombre
        self.año = año
        self.semestre = semestre
        self.creditos = creditos
        self.minimo = minimo
        self.profesor = None
        self.lista_de_alumnos = []
    
    def __str__(self):
        return f'Curso: {self.nombre} Año: {self.año} Semestre: {self.semestre}'

    def asignar_profesor(self, profesor):
        self.profesor = profesor
    
    def inscribir_alumno(self, alumno):
        self.lista_de_alumnos.append(alumno)
    
    def calcular_promedio(self):
        suma = 0
        for alumno in self.lista_de_alumnos:
            suma += alumno.calcular_promedio()
        return suma / len(self.lista_de_alumnos)

class Estudiante:

    def __init__(self, nombre, edad, numero_alumno, año):
        self.nombre = nombre
        self.edad = edad
        self.numero_alumno = numero_alumno
        self.año = año
        self.avance = 0
        self.notas = []
    
    def aprueba(self):
        return (sum(self.notas) / len(self.notas)) >= 3.95
    
    def estudiar(self, minutos):
        self.avance += 0.05 * minutos
    
    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)
    
    def __str__(self):
        return f'Estudiante: {self.nombre} Promedio: {self.calcular_promedio()}, Estado Aprobado: {self.aprueba()}'

class Profesor:
    
    def __init__(self, nombre, edad, oficina, departamento):
        self.nombre = nombre
        self.edad = edad
        self.oficina = oficina
        self.departamento = departamento
    
    def dictar_clase(self):
        print(f"El profesor {self.nombre} dicta una clase")
    
    def __str__(self):
        return f"{self.nombre} - oficina: {self.oficina}, Departamento: {self.departamento}"

if __name__ == "__main__":
    curso = Curso("Python", 2021, 2, 4, True)
    profe = Profesor("Juan", 35, "Calle Falsa 123", "Programacion")
    curso.asignar_profesor(profe)
    curso.profesor.dictar_clase()
    print(curso)