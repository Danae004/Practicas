"""
    Practicar con los codigos, explorar nuevas definiciones y aprender mas sobre python.
    PROBLEMA: Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

print("Bienvenido Humano :)")

try: edad =int(input("Ingresa tu edad por favor: "))
except ValueError:print("Al parecer no ingreso un numero")

    
if edad < 18 :
    print("¡Hey!, al parecer eres menor de edad")
else:
    print("¡Valla! Ya eres mayor de edad")

