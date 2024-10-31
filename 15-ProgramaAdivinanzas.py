# Juego de adivinanzas.
#Crea un juego donde el jugador debe adivinar un número secreto.
	#Puedes usar un ciclo while hasta que el jugador adivine correctamente.
	#El número secreto se puede crear utilizando la función randint para generar un numero aleatorio entre 1 y 70.
	#Por cada intento fallido se debe incrementar una variable que lleve el conteo de intentos.
	#El jugador pierde una vez superando los 7 intentos.
from random import randint

print("**Juego de adivinanzas**")

num_secreto = randint(1, 70)
intentos = 0
cant_intentos_maximos = 7
adivinanza = None

while adivinanza != num_secreto and intentos < cant_intentos_maximos:
    adivinanza = int(input("Adivina el número secreto (entre 1 y 70): "))
    intentos += 1 

    if adivinanza < num_secreto:
        print("El número secreto es mayor, sigue intentando.")
    elif adivinanza > num_secreto:
        print("El número secreto es menor, sigue intentando.")

if adivinanza == num_secreto:
    print(f"¡Enhorabuena! Has adivinado el número correcto en {intentos} intentos.")
else:
    print(f"Agotaste todos tus intentos máximos ({cant_intentos_maximos}).")
    print(f"El número secreto era: {num_secreto}.")