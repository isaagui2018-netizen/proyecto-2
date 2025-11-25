class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = None
        self.estudiantes = []

    def asignarProfesor(self, profesor):
        self.profesor = profesor

    def inscribirEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)


