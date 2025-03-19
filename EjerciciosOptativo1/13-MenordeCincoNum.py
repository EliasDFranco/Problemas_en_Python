#El menor de cinco números.
#Crear un programa para indicar cual es el menor de cinco números.
#El programa debe pedir al usuario cinco números enteros.
#Posteriormente se deben comparar y mandar a imprimir el número menor

print("Programa EL MENOR DE 5 NÚMEROS")

num_uno = int(input("Ingresar el 1er número: "))
num_dos = int(input("Ingresar el 2do número: "))
num_tres = int(input("Ingresar el 3er número: "))
num_cuatro = int(input("Ingresar el 4to número: "))
num_cinco = int(input("Ingresar el 5to número: "))

num_menor = num_uno

if num_dos  < num_menor:
    num_menor = num_dos
    
if num_tres < num_menor:
    num_menor = num_tres
      
if num_cuatro < num_menor:
    num_menor = num_cuatro
   
if num_cinco < num_menor:
    num_menor = num_cinco
       
print(f"El número menor de los cinco es: {num_menor} ")
