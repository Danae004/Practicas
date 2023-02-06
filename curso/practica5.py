
import random
 
intentosRealizados = 0
 
print("Hola, ¿cómo te llamas?")
nombre=input()
 
numero = random.randint(1,20)
print("Bueno, " + nombre + ", estoy pensando un número entre el 1 y el 20.")
 
while intentosRealizados < 5:
    print("Intenta adivinar: ")
    estimacion = input()
    estimacion = int(estimacion)
 
    if estimacion < numero:
        print("¡Tu número es muy bajo! ")
        intentosRealizados = intentosRealizados + 1
 
    if estimacion > numero:
        print("¡Tu número es muy alto! ")
        intentosRealizados = intentosRealizados + 1
 
    if estimacion == numero:
        intentosRealizados = intentosRealizados + 1
        break
 
 
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print("¡Buen trabajo, " + nombre + "! ¡Has adivinado el número en " + intentosRealizados + " intentos!")
 
if estimacion != numero:
    numero = str(numero)
    print("Lo siento. El número era " + numero)
