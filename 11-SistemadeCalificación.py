#Sistema de calificaciones
#Crear un programa para convertir una calificación numérica (entre 0 y 10) a una letra (de la F a la A)
#- Si es mayor o igual a 9 y menor o igual a 10 es una A.
#- Si es mayor o igual a 8 y menor a 9 es una B.
#- Si es mayor igual de 7 y menor a 8 es una C.
#- Si es mayor o igual a 6 y menor a 7 es una D.
#- Si es mayor o igual a 5 y menor a 6 es una E.
#- Si es mayor o igual a 0 menor a 6 es una F.
#- En otro caso, imprimir: “Valor desconocido”

print("***Sistema de Calificaciones***")

calificacion = float(input("Ingrese su calificación (0 a 10): "))

if 9 <= calificacion <= 10:
    letra = "A"
elif 8 <= calificacion < 9:
    letra = "B"
elif 7 <= calificacion < 8:
    letra = "C"
elif 6 <= calificacion < 7:
    letra = "D"
elif 5 <= calificacion < 6:
    letra = "E"
elif 0 <= calificacion < 6:
    letra = "F"
else:
    letra = None
    print("Valor desconocido")

if letra is not None:
    print(f"La calificación convertida en letra es: {letra}")