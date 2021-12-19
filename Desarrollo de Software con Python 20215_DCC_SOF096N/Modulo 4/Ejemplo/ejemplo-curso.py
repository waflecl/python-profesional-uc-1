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

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):

    def __init__(self, nombre, edad, numero_alumno, año):
        super().__init__(nombre, edad)
        self.numero_alumno = numero_alumno
        self.año = año
        self.avance = 0
        self.notas = []
    
    def aprueba(self):
        return (sum(self.notas) / len(self.notas)) >= 3.95
    
    def estudiar(self, minutos):
        self.avance += 0.05 * minutos
    
    def estudiar_en_grupo(self, alumno, minutos):
        self.avance += 0.1 * minutos
        alumno.avance += 0.1 * minutos
    
    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)
    
    def __str__(self):
        return f'Estudiante: {self.nombre} Promedio: {self.calcular_promedio()}, Estado Aprobado: {self.aprueba()}'

class Profesor(Persona):
    
    def __init__(self, nombre, edad, oficina, departamento):
        super().__init__(nombre, edad)
        self.oficina = oficina
        self.departamento = departamento
    
    def dictar_clase(self):
        print(f"El profesor {self.nombre} dicta una clase")
    
    def evaluar_estudiante(self, estudiante, nota):
        estudiante.notas.append(nota)
    
    def __str__(self):
        return f"{self.nombre} - oficina: {self.oficina}, Departamento: {self.departamento}"

if __name__ == "__main__":
    curso = Curso("Python", 2021, 2, 4, True)
    profe = Profesor("Juan", 35, "Calle Falsa 123", "Programacion")
    curso.asignar_profesor(profe)
    curso.profesor.dictar_clase()
    print(curso)

    est1 = Estudiante("Juan", 35, 1, 2021)
    est2 = Estudiante("Pedro", 25, 2, 2021)
    est3 = Estudiante("Maria", 20, 3, 2021)
    est4 = Estudiante("Jose", 30, 4, 2021)
    est5 = Estudiante("Ana", 25, 5, 2021)

    curso.inscribir_alumno(est1)
    curso.inscribir_alumno(est2)
    curso.inscribir_alumno(est3)
    curso.inscribir_alumno(est4)
    curso.inscribir_alumno(est5)

    profe.evaluar_estudiante(est1, 4.1)
    profe.evaluar_estudiante(est1, 6.9)
    profe.evaluar_estudiante(est1, 5.0)
    profe.evaluar_estudiante(est2, 3.9)
    profe.evaluar_estudiante(est2, 5.9)
    profe.evaluar_estudiante(est3, 3.5)
    profe.evaluar_estudiante(est3, 2.9)
    profe.evaluar_estudiante(est4, 5.7)
    profe.evaluar_estudiante(est5, 6.8)
    profe.evaluar_estudiante(est5, 4.9)
    profe.evaluar_estudiante(est5, 5.9)

    print(f"Promedio del curso: {curso.calcular_promedio()}")

    print(est1)
    print(est2)
    print(est3)
    print(est4)
    print(est5)
