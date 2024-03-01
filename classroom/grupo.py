from classroom.asignatura import Asignatura

class Grupo:
    
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes = ["Grupo de estudiantes:"]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))
            
    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos = lista[0:]
        lista.pop(0)
        
        

    def __str__(self) -> str:
        cadena = self.listadoAlumnos[0]+" "+self._grupo
        return cadena #revisar aca
        pass
        

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
