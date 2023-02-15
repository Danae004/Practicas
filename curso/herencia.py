"""
Nombre: Josandy Danae B.A.
FECHA: 14/02/23
DESCRIPCION: En esta etapa veremos todo lo relacionado con "POO"
"""



class Persona:
    __nombre=None
    __email=None
    def __init__(self):
        print("persona")

class Alumno (Persona):
     __nombre=None
     __matricula=None
     __carrera=None
     def __init__(self):
         super().__init__()
         print("Alumno")

objeto_persona= Persona()
objeto_alumno= Alumno()

objeto_persona.nombre= "Dejah"
print(objeto_persona.nombre)

objeto_alumno.nombre= "John Carter"
print(objeto_alumno.nombre)

objeto_alumno.email= "john@utectulancingo.edu.mx"
print(objeto_alumno.email)

print(dir(objeto_persona))
print(dir(objeto_alumno))