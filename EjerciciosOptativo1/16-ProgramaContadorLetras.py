#Verificación de letras.
#Escribir un programa en el que se pregunte al usuario 
#por una frase y una letra,
#y muestre por pantalla el número de veces que aparece 
#la letra en la frase

print("**Contador de las letras en una frase**")

cont = 0
frase = input("Introduzca una frase: ")
letra = input("Introduzca una letra: ")

if len(letra) != 1:
    print("Introduzca una sola letra")
else: 
    cont = frase.lower().count(letra.lower())

print(f"La letra: {letra}, está en {cont} veces en la frase ")